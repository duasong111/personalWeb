from bson import ObjectId

from otherFunctions.create_response import create_response
from flask import Flask, request, jsonify, Response
from secuty import generate_jwt_token,verify_jwt_token
from typing import Optional, Tuple
from datetime import datetime, timedelta
import bcrypt
from http import HTTPStatus
app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login(users=None, user_data=None) -> Tuple[Response, int]:
    """处理用户登录请求，返回 JWT token"""
    try:
        # 获取请求数据
        return_data: dict = request.get_json(silent=True)
        print("传输来的数据:",return_data)
        if not return_data:
            return create_response(HTTPStatus.BAD_REQUEST, "请求数据格式错误", False)

        username: str = return_data.get("username", "").strip()
        password: str = return_data.get("password", "")

        if not username or not password:
            return create_response(HTTPStatus.BAD_REQUEST, "用户名和密码为必填项", False)

        # 查询用户
        user = users.find_one({"username": username})
        if not user:
            return create_response(HTTPStatus.NOT_FOUND, "用户不存在", False)

        # 验证密码
        stored_password: bytes = user["password"].encode("utf-8")
        if not bcrypt.checkpw(password.encode("utf-8"), stored_password):
            return create_response(HTTPStatus.UNAUTHORIZED, "密码错误", False)
        # 更新最后登录时间
        users.update_one(
            {"username": username},
            {"$set": {"lastLogin": datetime.utcnow()}}
        )
        # 生成 JWT token
        token = generate_jwt_token(str(user["_id"]))

        # 返回成功响应，适配你的数据结构
        return create_response(HTTPStatus.OK, "登录成功", True, data=user_data)

    except Exception as e:
        return create_response(HTTPStatus.INTERNAL_SERVER_ERROR, f"服务器错误: {str(e)}", False)

@app.route("/protected", methods=["GET"])
def protected_route(users=None) -> Tuple[Response, int]:
    """需要 JWT 认证的路由"""
    token = request.headers.get("Authorization")
    if not token:
        return create_response(HTTPStatus.UNAUTHORIZED, "缺少认证令牌", False)

    # 假设 token 格式为 "Bearer <token>"
    if token.startswith("Bearer "):
        token = token[7:]

    payload = verify_jwt_token(token)
    if not payload:
        return create_response(HTTPStatus.UNAUTHORIZED, "令牌无效或已过期", False)

    user_id = payload["user_id"]
    user = users.find_one({"_id": ObjectId(user_id)})
    if not user:
        return create_response(HTTPStatus.NOT_FOUND, "用户不存在", False)
if __name__ == '__main__':
    app.run()
