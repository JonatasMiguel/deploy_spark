import os
from flask import jsonify, request, Flask, send_file

HTTP_STATUS_CODE_SUCCESS = 200
HTTP_STATUS_CODE_SUCCESS_CREATED = 201
HTTP_STATUS_CODE_CONFLICT = 409
HTTP_STATUS_CODE_NOT_ACCEPTABLE = 406
HTTP_STATUS_CODE_NOT_FOUND = 404

SAMPLE_HOST_IP = "SAMPLE_HOST_IP"
SAMPLE_HOST_PORT = "SAMPLE_HOST_PORT"
SAMPLE_HOST_NAME = "SAMPLE_HOST_NAME"

app = Flask(__name__)

@app.route("/")
def index():
    return f"<html> <h1> HELLO, WORLD </h1> </html>"


if __name__ == "__main__":
    app.run(host=os.environ[SAMPLE_HOST_IP],
            port=int(os.environ[SAMPLE_HOST_PORT]))

