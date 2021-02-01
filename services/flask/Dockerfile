FROM spark_task_image

WORKDIR /usr/src/flask
COPY . /usr/src/flask

RUN pip install flask==1.1.2

ENV SAMPLE_HOST_NAME "flask"
ENV SAMPLE_HOST_PORT 5005
ENV SAMPLE_HOST_IP "0.0.0.0"
ENV SPARK_MASTER_HOST "sparkmaster"
ENV SPARK_MASTER_PORT 7077
ENV SPARK_DRIVER_PORT 41105
CMD ["python", "server.py"]