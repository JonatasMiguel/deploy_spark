echo "--------------------------------------------------------------------"
echo "Buiding the images..."
echo "--------------------------------------------------------------------"


docker image build --tag spark_task_image services/spark_task_image

docker image build --tag spark_image services/spark_image

docker image build --tag twitter_image services/twitter

docker image build --tag dashboards_image services/dashboards

docker image build --tag streaming_image services/streaming

docker network create -d overlay --subnet=192.168.0.1/24 --gateway=192.168.0.1 --attachable cluster_network

