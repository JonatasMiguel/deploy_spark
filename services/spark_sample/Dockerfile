FROM spark_task_image

WORKDIR /usr/src/spark-sample
COPY . /usr/src/spark-sample

RUN pip install flask==1.1.2

ENV SAMPLE_HOST_NAME "spark-sample"
ENV SAMPLE_HOST_PORT 5005
ENV SAMPLE_HOST_IP "0.0.0.0"
ENV SPARK_MASTER_HOST "sparkmaster"
ENV SPARK_MASTER_PORT 7077
ENV SPARK_DRIVER_PORT 41105
CMD ["python", "server.py"]