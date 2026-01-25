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
PRIMARY_NS = {"common": "http://linux.duke.edu/metadata/common"}


def download(url):
    with urllib.request.urlopen(url) as r:
        return r.read()


def write_file(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)


def parse_repomd(repomd_xml):
    root = ET.fromstring(repomd_xml)
    for data in root.findall("repo:data", REPO_NS):
        if data.get("type") == "primary":
            loc = data.find("repo:location", REPO_NS)
            if loc is not None and loc.get("href"):
                return loc.get("href")
    return None


def parse_primary(primary_xml, pkg_names):
    root = ET.fromstring(primary_xml)
    results = {}
    for pkg in root.findall("common:package", PRIMARY_NS):
        name_el = pkg.find("common:name", PRIMARY_NS)
        if name_el is None:
            continue
        name = name_el.text or ""
        if name not in pkg_names:
            continue
        time_el = pkg.find("common:time", PRIMARY_NS)
        build_time = 0
        if time_el is not None and time_el.get("build"):
            try:
                build_time = int(time_el.get("build"))
            except ValueError:
                build_time = 0
        loc_el = pkg.find("common:location", PRIMARY_NS)
        if loc_el is None or not loc_el.get("href"):
            continue
        ver_el = pkg.find("common:version", PRIMARY_NS)
        ver_str = ""
        if ver_el is not None:
            epoch = ver_el.get("epoch", "0")
            ver = ver_el.get("ver", "")
            rel = ver_el.get("rel", "")
            ver_str = f"{epoch}:{ver}-{rel}"
        current = results.get(name)
        if current is None or build_time > current["build_time"]:
            results[name] = {
                "build_time": build_time,
                "href": loc_el.get("href"),
                "version": ver_str,
            }
    return results


def main():
    parser = argparse.ArgumentParser(description="Prepare offline Docker RPM bundle (aarch64)")
    parser.add_argument("--output", required=True, help="output directory")
    parser.add_argument("--repo-base", required=True, help="repo base url, e.g. https://download.docker.com/linux/centos/8/aarch64/stable/")
    parser.add_argument("--packages", nargs="+", required=True, help="package names to download")
    parser.add_argument("--primary-cache", default="", help="optional local primary.xml.gz cache path")
    args = parser.parse_args()

    repo_base = args.repo_base.rstrip("/") + "/"
    os.makedirs(args.output, exist_ok=True)

    repomd_url = urljoin(repo_base, "repodata/repomd.xml")
    repomd_xml = download(repomd_url)
    primary_href = parse_repomd(repomd_xml)
    if not primary_href:
        print("Failed to locate primary.xml in repomd", file=sys.stderr)
        return 2

    primary_url = urljoin(repo_base, primary_href)
    if args.primary_cache and os.path.exists(args.primary_cache):
        with open(args.primary_cache, "rb") as f:
            primary_gz = f.read()
    else:
        primary_gz = download(primary_url)
    primary_xml = gzip.decompress(primary_gz)

    pkg_names = set(args.packages)
    selected = parse_primary(primary_xml, pkg_names)
    missing = [p for p in args.packages if p not in selected]
    if missing:
        print("Missing packages in repo: " + ", ".join(missing), file=sys.stderr)
        return 3

    manifest_lines = []
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    manifest_lines.append(f"bundle_generated_at={ts}")
    manifest_lines.append(f"repo_base={repo_base}")

    for name in args.packages:
        entry = selected[name]
        href = entry["href"]
        url = urljoin(repo_base, href)
        filename = os.path.basename(href)
        dest = os.path.join(args.output, filename)
        data = download(url)
        write_file(dest, data)
        manifest_lines.append(f"{name}={entry['version']}|{filename}|")

    manifest_path = os.path.join(args.output, "bundle_manifest.txt")
    with open(manifest_path, "w", encoding="utf-8") as f:
        f.write("\n".join(manifest_lines) + "\n")

    print(f"Downloaded {len(args.packages)} packages to {args.output}")
    print("Manifest: " + manifest_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
