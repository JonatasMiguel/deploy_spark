echo "--------------------------------------------------------------------"
echo "Buiding the images..."
echo "--------------------------------------------------------------------"


docker build --tag spark_task_image services/spark_task_image

docker build --tag spark_image services/spark_image

docker build --tag twitter_image services/twitter_client

docker build --tag dashboards_image services/dashboards

docker build --tag streaming_image services/streaming


