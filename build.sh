echo "--------------------------------------------------------------------"
echo "Buiding the images..."
echo "--------------------------------------------------------------------"


docker image build --tag spark_task_image services/spark_task_image

docker image build --tag spark_image services/spark_image

docker image build --tag twitter_image services/twitter

docker image build --tag dashboards_image services/dashboards

docker image build --tag streaming_image services/streaming


