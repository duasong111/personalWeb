from bson import ObjectId
from otherFunctions.create_response import create_response
from flask import Flask, request, jsonify, Response
from typing import Optional, Tuple
from functions.userLogin import LoginFunction
import bcrypt
from http import HTTPStatus
app = Flask(__name__)
checkLogin = LoginFunction()
@app.route("/login", methods=["POST"],strict_slashes=False)
def login():
    try:
        data = request.get_json()  # 解析 JSON 数据
        user = data.get('user')
        pwd = data.get('pwd')
        return checkLogin.checklogin(user,pwd)
    except Exception as e:
        return create_response(HTTPStatus.INTERNAL_SERVER_ERROR, f"服务器错误: {str(e)}", False)


@app.route("/", methods=["GET"])
def index():
        return "success"



if __name__ == '__main__':
    app.run()
