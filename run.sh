#!/bin/bash

echo "--------------------------------------------------------------------"
echo "Buiding the images..."
echo "--------------------------------------------------------------------"

docker build --tag spark_task_image services/spark_task_image

docker build --tag spark_image services/spark_image

docker build --tag twitter_image services/twitter

docker build --tag dashboards_image services/dashboards

docker build --tag streaming_image services/streaming

echo "--------------------------------------------------------------------"
echo "Pushing to dockerhub..."
echo "--------------------------------------------------------------------"

docker tag spark_task_image jonatasmiguel/spark_task_image:latest
docker push jonatasmiguel/spark_task_image

docker tag spark_image jonatasmiguel/spark_image:latest
docker push jonatasmiguel/spark_image

docker tag twitter_image jonatasmiguel/twitter_image:latest
docker push jonatasmiguel/twitter_image

docker tag dashboards_image jonatasmiguel/dashboards_image:latest
docker push jonatasmiguel/dashboards_image

docker tag streaming_image jonatasmiguel/streaming_image:latest
docker push jonatasmiguel/streaming_image

docker-compose build

echo "--------------------------------------------------------------------"
echo "Restarting docker service..."
echo "--------------------------------------------------------------------"

service docker restart

echo "--------------------------------------------------------------------"
echo "Network..."
echo "--------------------------------------------------------------------"



echo "--------------------------------------------------------------------"
echo "Deploying in swarm cluster..."
echo "--------------------------------------------------------------------"

docker stack deploy --compose-file=docker-compose.yml swarm
docker stack services swarm

echo "--------------------------------------------------------------------"
echo "End."
echo "--------------------------------------------------------------------"