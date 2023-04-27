# Zsu
Creating an XML helper application to ease my Sisters life.

1., build from Dockerfile and app folder

docker build -t gdocker .  

2., tag image
docker tag gdocker glizik/gdocker

3., push to docker hub
docker push glizik/gdocker 

4., run deploy script
cat ./server_deploy.sh | sshpass -p Barack57 ssh root@192.168.135.4


4+1., manually deploy: ssh to NAS
    ssh root@192.168.135.4

    pull image
    docker pull glizik/gdocker
    docker stop gcontainer
    docker rm gcontainer
    docker run -d -p 5577:22 -p 49153:80 --volume=/docker:/docker --name gcontainer glizik/gdocker:latest
