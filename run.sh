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

docker tag local-image:spark_task_image jonatasmiguelsd:spark_task_image
docker push jonatasmiguelsd:spark_task_image

docker tag local-image:spark_image jonatasmiguelsd:spark_image
docker push jonatasmiguelsd:spark_image

docker tag local-image:twitter_image jonatasmiguelsd:twitter_image
docker push jonatasmiguelsd:twitter_image

docker tag local-image:dashboards_image jonatasmiguelsd:dashboards_image
docker push jonatasmiguelsd:dashboards_image

docker tag local-image:streaming_image jonatasmiguelsd:streaming_image
docker push jonatasmiguelsd:streaming_image

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