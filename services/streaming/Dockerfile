FROM spark_task_image

WORKDIR /usr/src/stream
COPY . /usr/src/stream

RUN pip install flask==1.1.2
RUN pip install requests

ENV SAMPLE_HOST_NAME "streaming"
ENV SAMPLE_HOST_PORT 5005
ENV SAMPLE_HOST_IP "0.0.0.0"

ENV SPARK_MASTER_HOST "sparkmaster"
ENV SPARK_MASTER_PORT 7077
ENV SPARK_DRIVER_PORT 41100

ENV TWITTER_CLIENT "twitter"
ENV TWITTER_PORT 9017

ENV DASHBOARD_CLIENT "dashboards"
ENV DASHBOARD_PORT 5009


CMD ["python", "server.py"]