import os
from pyspark.context import SparkContext
from pyspark.sql import SparkSession

HELLO_HOST_IP = "HELLO_HOST_IP"
HELLO_HOST_PORT = "HELLO_HOST_PORT"
HELLO_HOST_NAME = "HELLO_HOST_NAME"

SPARK_MASTER_HOST = "SPARK_MASTER_HOST"
SPARK_MASTER_PORT = "SPARK_MASTER_PORT"
SPARK_DRIVER_PORT = "SPARK_DRIVER_PORT"

def inside(p):
    x, y = os.urandom.random(), os.urandom.random()
    return x*x + y*y < 1

ss = (
    SparkSession
    .builder
    .appName("helloworld")
    .config("spark.driver.port", os.environ[SPARK_DRIVER_PORT])
    .config("spark.driver.host", os.environ[HELLO_HOST_NAME])
    .master("spark://"
            + os.environ[SPARK_MASTER_HOST]
            + ":"
            + str(os.environ[SPARK_MASTER_PORT])
            )
    .getOrCreate()
)


sc: SparkContext = ss.sparkContext
count = sc.parallelize(range(0, 100)) \
    .filter(inside).count()

print(f"Pi is roughly {4.0*count / 100}")
