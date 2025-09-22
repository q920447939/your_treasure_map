pwd
cp ../deploy/docker-compose-linux-x86_64 ./
mv docker-compose-linux-x86_64 docker-compose
mv docker-compose /usr/local/bin/
cd /usr/local/bin/
chmod +x /usr/local/bin/docker-compose

docker-compose --version
