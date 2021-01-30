#!/bin/bash

echo "--------------------------------------------------------------------"
echo "Buiding the images..."
echo "--------------------------------------------------------------------"

docker build --tag spark_task services/spark_task_image
docker push 127.0.0.1:5050/spark_task

docker build --tag spark services/spark_image
docker push 127.0.0.1:5050/spark

docker-compose build

echo "--------------------------------------------------------------------"
echo "Restarting docker service..."
echo "--------------------------------------------------------------------"

service docker restart

echo "--------------------------------------------------------------------"
echo "Deploying in swarm cluster..."
echo "--------------------------------------------------------------------"

docker stack deploy --compose-file=docker-compose.yml microservices
docker stack services microservices

echo "--------------------------------------------------------------------"
echo "End."
echo "--------------------------------------------------------------------"