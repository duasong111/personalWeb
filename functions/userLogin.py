from otherFunctions.create_response import create_response
from flask import Flask, request, jsonify, Response
from secuty import generate_jwt_token,verify_jwt_token
from datetime import datetime, timedelta
from database.operateFunction import execuFunction as dbFunction
import bcrypt
from http import HTTPStatus
# 检查用户是否登录成功的函数
class LoginFunction():

    def checklogin(self,username=None,password=None):
        try:
            # 获取请求数据
            return_data: dict = request.get_json(silent=True)
            print("传输来的数据:", return_data)
            if not return_data:
                return create_response(HTTPStatus.BAD_REQUEST, "请求数据格式错误", False)
            username: str = return_data.get("username", "").strip()
            password: str = return_data.get("password", "")
            if not username or not password:
                return create_response(HTTPStatus.BAD_REQUEST, "用户名和密码为必填项", False)
            # 查询用户
            queryResult = dbFunction.query_individual_users(dbName='user',queryParams="username",queryData=username)

            print("查看从数据库中返回的结果",queryResult)
            # if not queryResult:
            #     return create_response(HTTPStatus.NOT_FOUND, "用户不存在", False)
            # # 验证密码
            # stored_password: bytes = user["password"].encode("utf-8")
            # if not bcrypt.checkpw(password.encode("utf-8"), stored_password):
            #     return create_response(HTTPStatus.UNAUTHORIZED, "密码错误", False)
            # 更新最后登录时间
            # users.update_one(
            #     {"username": username},
            #     {"$set": {"lastLogin": datetime.utcnow()}}
            # )
            # 生成 JWT token
            # token = generate_jwt_token(str(user["_id"]))

            # 返回成功响应，适配你的数据结构
            return create_response(HTTPStatus.OK, "登录成功", True)

        except Exception as e:
            return create_response(HTTPStatus.INTERNAL_SERVER_ERROR, f"服务器错误: {str(e)}", False)
