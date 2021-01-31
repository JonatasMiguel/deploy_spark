#!/bin/bash

echo "--------------------------------------------------------------------"
echo "Buiding the images..."
echo "--------------------------------------------------------------------"

docker build --tag spark_task_image services/spark_task_image

docker build --tag spark_image services/spark_image

docker-compose build

echo "--------------------------------------------------------------------"
echo "Restarting docker service..."
echo "--------------------------------------------------------------------"

service docker restart

echo "--------------------------------------------------------------------"
echo "Deploying in swarm cluster..."
echo "--------------------------------------------------------------------"

docker stack deploy --compose-file=docker-compose.yml swarm
docker stack services swarm

echo "--------------------------------------------------------------------"
echo "End."
echo "--------------------------------------------------------------------"