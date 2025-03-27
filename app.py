from bson import ObjectId

from otherFunctions.create_response import create_response
from flask import Flask, request, jsonify, Response
from secuty import generate_jwt_token,verify_jwt_token
from typing import Optional, Tuple
from functions.userLogin import LoginFunction as checkLogin
import bcrypt
from http import HTTPStatus
app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login(user=None, pwd=None):
    try:
        return checkLogin.checklogin(user,pwd)
    except Exception as e:
        return create_response(HTTPStatus.INTERNAL_SERVER_ERROR, f"服务器错误: {str(e)}", False)

if __name__ == '__main__':
    app.run()
