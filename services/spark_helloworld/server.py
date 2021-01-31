import os
from flask import jsonify, request, Flask, send_file
from pyspark.context import SparkContext
from pyspark.sql import SparkSession

HTTP_STATUS_CODE_SUCCESS = 200
HTTP_STATUS_CODE_SUCCESS_CREATED = 201
HTTP_STATUS_CODE_CONFLICT = 409
HTTP_STATUS_CODE_NOT_ACCEPTABLE = 406
HTTP_STATUS_CODE_NOT_FOUND = 404

HELLO_HOST_IP = "HELLO_HOST_IP"
HELLO_HOST_PORT = "HELLO_HOST_PORT"

SPARKMASTER_HOST = "SPARKMASTER_HOST"
SPARKMASTER_PORT = "SPARKMASTER_PORT"
SPARK_DRIVER_PORT = "SPARK_DRIVER_PORT"


ss = (
    SparkSession
        .builder
        .appName("helloworld")
        .config("spark.driver.port", os.environ["SPARK_DRIVER_PORT"])
        .config("spark.driver.host", os.environ["HELLO_HOST_NAME"])
        .master(
            f"spark://{os.environ[SPARKMASTER_HOST]}:{os.os.environ[SPARKMASTER_PORT]}"
        )
        .getOrCreate()
)


app = Flask(__name__)

@app.route("/helloworld", methods=["GET"])
def hello_world():
    def inside(p):
        x, y = os.urandom.random(), os.urandom.random()
        return x*x + y*y < 1

    sc: SparkContext = ss.sparkContext
    count = sc.parallelize(range(0, 100)) \
                .filter(inside).count()

    return (
        jsonify({
            "result": f"Pi is roughly {4.0*count / 100}" }),
        HTTP_STATUS_CODE_SUCCESS_CREATED,
    )


if __name__ == "__main__":
    app.run(host=os.environ[HELLO_HOST_IP],
            port=int(os.environ[HELLO_HOST_PORT]))