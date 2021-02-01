import os
from flask import jsonify, request, Flask, send_file
from pyspark.context import SparkContext
from pyspark.sql import SparkSession

HTTP_STATUS_CODE_SUCCESS = 200
HTTP_STATUS_CODE_SUCCESS_CREATED = 201
HTTP_STATUS_CODE_CONFLICT = 409
HTTP_STATUS_CODE_NOT_ACCEPTABLE = 406
HTTP_STATUS_CODE_NOT_FOUND = 404

SAMPLE_HOST_IP = "SAMPLE_HOST_IP"
SAMPLE_HOST_PORT = "SAMPLE_HOST_PORT"
SAMPLE_HOST_NAME = "SAMPLE_HOST_NAME"

SPARK_MASTER_HOST = "SPARK_MASTER_HOST"
SPARK_MASTER_PORT = "SPARK_MASTER_PORT"
SPARK_DRIVER_PORT = "SPARK_DRIVER_PORT"

app = Flask(__name__)

@app.route("/")
def index():
    return f"<html> <h1> HELLO, WORLD </h1> </html>"


@app.route("/<int:pirange>")
def hello_world(pirange):
    def inside(p):
        x, y = os.urandom.random(), os.urandom.random()
        return x*x + y*y < 1

    ss = (
        SparkSession
            .builder
            .appName("helloworld")
            .config("spark.driver.port", os.environ[SPARK_DRIVER_PORT])
            .config("spark.driver.host", os.environ[SAMPLE_HOST_NAME])
            .master("spark://"
                    + os.environ[SPARK_MASTER_HOST]
                    + ":"
                    + str(os.environ[SPARK_MASTER_PORT])
                    )
            .getOrCreate()
    )


    sc: SparkContext = ss.sparkContext
    count = sc.parallelize(range(0, pirange)) \
                .filter(inside).count()

    ss.stop()

    return f"<html> <h1> Pi is roughly {4.0*count / 100} </h1> </html>"


if __name__ == "__main__":
    app.run(host=os.environ[SAMPLE_HOST_IP],
            port=int(os.environ[SAMPLE_HOST_PORT]))

