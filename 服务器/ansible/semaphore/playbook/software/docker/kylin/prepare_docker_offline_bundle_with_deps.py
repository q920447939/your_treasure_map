#!/usr/bin/env python3
import argparse
import gzip
import os
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from urllib.parse import urljoin

REPO_NS = {"repo": "http://linux.duke.edu/metadata/repo"}
COMMON_NS = {"common": "http://linux.duke.edu/metadata/common"}
RPM_NS = {"rpm": "http://linux.duke.edu/metadata/rpm"}


def download(url, timeout=30, retries=3, backoff=2):
    last_err = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(url, timeout=timeout) as r:
                return r.read()
        except Exception as e:
            last_err = e
            if attempt < retries - 1:
                time.sleep(backoff)
    raise last_err


def parse_repomd(repomd_xml):
    root = ET.fromstring(repomd_xml)
    primary = None
    filelists = None
    for data in root.findall("repo:data", REPO_NS):
        dtype = data.get("type")
        loc = data.find("repo:location", REPO_NS)
        if loc is None or not loc.get("href"):
            continue
        href = loc.get("href")
        if dtype == "primary":
            primary = href
        elif dtype == "filelists":
            filelists = href
    return primary, filelists


def load_primary(repo_base, primary_href):
    xml_gz = download(urljoin(repo_base, primary_href))
    xml = gzip.decompress(xml_gz)
    root = ET.fromstring(xml)
    packages = []
    for pkg in root.findall("common:package", COMMON_NS):
        name_el = pkg.find("common:name", COMMON_NS)
        arch_el = pkg.find("common:arch", COMMON_NS)
        ver_el = pkg.find("common:version", COMMON_NS)
        loc_el = pkg.find("common:location", COMMON_NS)
        time_el = pkg.find("common:time", COMMON_NS)
        if name_el is None or arch_el is None or ver_el is None or loc_el is None:
            continue
        name = name_el.text or ""
        arch = arch_el.text or ""
        epoch = ver_el.get("epoch", "0")
        ver = ver_el.get("ver", "")
        rel = ver_el.get("rel", "")
        href = loc_el.get("href", "")
        build_time = 0
        if time_el is not None and time_el.get("build"):
            try:
                build_time = int(time_el.get("build"))
            except ValueError:
                build_time = 0

        # requires
        requires = []
        fmt = pkg.find("common:format", COMMON_NS)
        if fmt is not None:
            reqs = fmt.find("rpm:requires", RPM_NS)
            if reqs is not None:
                for ent in reqs.findall("rpm:entry", RPM_NS):
                    rname = ent.get("name", "")
                    if not rname or rname.startswith("rpmlib("):
                        continue
                    requires.append({
                        "name": rname,
                        "flags": ent.get("flags"),
                        "epoch": ent.get("epoch"),
                        "ver": ent.get("ver"),
                        "rel": ent.get("rel"),
                    })

        # provides
        provides = []
        if fmt is not None:
            provs = fmt.find("rpm:provides", RPM_NS)
            if provs is not None:
                for ent in provs.findall("rpm:entry", RPM_NS):
                    pname = ent.get("name", "")
                    if pname:
                        provides.append(pname)

        packages.append({
            "name": name,
            "arch": arch,
            "epoch": epoch,
            "ver": ver,
            "rel": rel,
            "href": href,
            "build": build_time,
            "requires": requires,
            "provides": provides,
        })
    return packages


def load_filelists(repo_base, filelists_href):
    xml_gz = download(urljoin(repo_base, filelists_href))
    xml = gzip.decompress(xml_gz)
    root = ET.fromstring(xml)
    filemap = {}
    for pkg in root.findall("common:package", COMMON_NS):
        name_el = pkg.find("common:name", COMMON_NS)
        arch_el = pkg.find("common:arch", COMMON_NS)
        if name_el is None or arch_el is None:
            continue
        name = name_el.text or ""
        arch = arch_el.text or ""
        for f in pkg.findall("common:file", COMMON_NS):
            path = f.text or ""
            if not path:
                continue
            # keep first provider; we'll resolve by latest build later
            filemap.setdefault(path, []).append((name, arch))
    return filemap


def main():
    parser = argparse.ArgumentParser(description="Prepare offline Docker RPM bundle with deps")
    parser.add_argument("--output", required=True, help="output directory")
    parser.add_argument("--repos", nargs="+", required=True, help="repo base urls")
    parser.add_argument("--packages", nargs="+", required=True, help="package names to download")
    parser.add_argument("--arch", default="aarch64", help="target arch")
    parser.add_argument("--include-noarch", action="store_true", help="include noarch packages")
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)
    allowed_arch = {args.arch}
    if args.include_noarch:
        allowed_arch.add("noarch")

    all_packages = []
    filelists_maps = []

    for repo in args.repos:
        repo_base = repo.rstrip("/") + "/"
        repomd = download(urljoin(repo_base, "repodata/repomd.xml"))
        primary_href, filelists_href = parse_repomd(repomd)
        if not primary_href:
            print(f"Failed to find primary.xml for {repo_base}", file=sys.stderr)
            return 2
        pkgs = load_primary(repo_base, primary_href)
        for p in pkgs:
            p["repo_base"] = repo_base
        all_packages.extend(pkgs)
        if filelists_href:
            filelists_maps.append((repo_base, load_filelists(repo_base, filelists_href)))

    # index packages by (name, arch)
    pkg_by_name = {}
    for p in all_packages:
        if p["arch"] not in allowed_arch:
            continue
        pkg_by_name.setdefault(p["name"], []).append(p)

    # choose latest by build time
    def latest_pkg(name):
        lst = pkg_by_name.get(name, [])
        if not lst:
            return None
        return max(lst, key=lambda x: x.get("build", 0))

    # provides index
    provides = {}
    for p in all_packages:
        if p["arch"] not in allowed_arch:
            continue
        # self provide
        provides.setdefault(p["name"], []).append(p)
        for prov in p.get("provides", []):
            provides.setdefault(prov, []).append(p)

    # file provides map
    file_provides = {}
    for repo_base, fmap in filelists_maps:
        for path, providers in fmap.items():
            for name, arch in providers:
                if arch not in allowed_arch:
                    continue
                # map file -> package list
                file_provides.setdefault(path, set()).add(name)

    def pick_provider(req_name):
        # file requirement
        if req_name.startswith("/"):
            names = list(file_provides.get(req_name, []))
            for nm in names:
                pkg = latest_pkg(nm)
                if pkg:
                    return pkg
            return None
        # normal provide
        lst = provides.get(req_name, [])
        if not lst:
            return None
        return max(lst, key=lambda x: x.get("build", 0))

    # resolve deps
    target_names = list(args.packages)
    resolved = {}
    queue = []
    for name in target_names:
        pkg = latest_pkg(name)
        if not pkg:
            print(f"Missing package in repos: {name}", file=sys.stderr)
            return 3
        key = (pkg["name"], pkg["arch"], pkg["ver"], pkg["rel"])
        if key not in resolved:
            resolved[key] = pkg
            queue.append(pkg)

    while queue:
        pkg = queue.pop(0)
        for req in pkg.get("requires", []):
            req_name = req.get("name")
            if not req_name:
                continue
            prov = pick_provider(req_name)
            if not prov:
                # allow missing for kernel modules etc
                continue
            key = (prov["name"], prov["arch"], prov["ver"], prov["rel"])
            if key in resolved:
                continue
            resolved[key] = prov
            queue.append(prov)

    # download packages
    manifest_lines = []
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    manifest_lines.append(f"bundle_generated_at={ts}")
    manifest_lines.append("repos=" + ";".join([r.rstrip("/") for r in args.repos]))
    manifest_lines.append("packages=" + ",".join(args.packages))

    for key, p in sorted(resolved.items(), key=lambda x: x[0][0]):
        url = urljoin(p["repo_base"], p["href"])
        filename = os.path.basename(p["href"])
        dest = os.path.join(args.output, filename)
        if not os.path.exists(dest):
            data = download(url, timeout=60)
            with open(dest, "wb") as f:
                f.write(data)
        manifest_lines.append(f"{p['name']}={p['epoch']}:{p['ver']}-{p['rel']}|{filename}|")

    manifest_path = os.path.join(args.output, "bundle_manifest.txt")
    with open(manifest_path, "w", encoding="utf-8") as f:
        f.write("\n".join(manifest_lines) + "\n")

    print(f"Downloaded {len(resolved)} packages to {args.output}")
    print("Manifest: " + manifest_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
