#!/bin/bash

echo "--------------------------------------------------------------------"
echo "Buiding the images..."
echo "--------------------------------------------------------------------"

docker build --tag spark_task_image services/spark_task_image

docker build --tag spark_image services/spark_image

docker build --tag twitter_image services/twitter

docker build --tag dashboards_image services/dashboards

docker build --tag streaming_image services/streaming



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