#!/bin/bash

# Pull the latest image
docker pull glizik/gdocker:latest

# Stop the current container
docker stop gcontainer
sleep 5

# Remove the current container
docker rm gcontainer
sleep 5

# Run the new image as a container
docker run -d -p 5577:22 -p 49153:80 --volume=/docker:/docker --name gcontainer glizik/gdocker:latest
