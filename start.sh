#! /bin/bash

DATA=$1
PORT=$2
TAG=$3

cd docker_build
if [ $# -eq 4 ]; then
	if [ "$4" = "--build" ]; then
		# Build the docker container
		docker build -f Dockerfile.dev -t $TAG .
	fi
fi
cd ..

# Run the docker container. Add additional -v if
# you need to mount more volumes into the container
# Also, make sure to edit the ports to fix your needs.
docker run -d --gpus all -it -p $PORT:8888 -v $(pwd):/tf/work		\
	-v $DATA:/tf/data --user $(id -u):$(id -g) --name $TAG $TAG
