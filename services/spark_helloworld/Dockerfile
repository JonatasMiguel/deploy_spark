FROM spark_task_image

WORKDIR /usr/src/helloworld
COPY . /usr/src/helloworld

RUN pip install flask==1.1.2

ENV HELLO_HOST_NAME "swarm_helloworld"
ENV HELLO_HOST_PORT 5005
ENV HELLO_HOST_IP "0.0.0.0"
ENV SPARKMASTER_HOST "swarm_sparkmaster"
ENV SPARKMASTER_PORT 7077
ENV SPARK_DRIVER_PORT 41200
CMD ["python", "server.py"]