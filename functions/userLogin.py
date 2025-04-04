from otherFunctions.create_response import create_response
from flask import Flask, request, jsonify, Response
import secrets
from datetime import datetime, timedelta
from database.operateFunction import execuFunction
import bcrypt
from http import HTTPStatus
# 检查用户是否登录成功的函数
class LoginFunction():

    def checklogin(self,username=None,password=None):
        try:
            # 获取请求数据
            return_data: dict = request.get_json(silent=True)
            if not return_data:
                return create_response(HTTPStatus.BAD_REQUEST, "请求数据格式错误", False)
            username: str = return_data.get("username", "").strip()
            password: str = return_data.get("password", "")
            if not username or not password:
                return create_response(HTTPStatus.BAD_REQUEST, "用户名和密码为必填项", False)
            # 查询用户-首先先去实例化一下
            dbFunction = execuFunction()
            queryResult = dbFunction.query_individual_users(dbName='users',queryParams="username",queryData=username)
            new_token = secrets.token_hex(16)  # 生成一个 32 字符的随机十六进制 token

            # 3. 更新数据库中的 token
            update_result = dbFunction.update_user_token(dbName='users', username=username, new_token=new_token)
            print("查看更新的情况:",update_result)

            return create_response(HTTPStatus.OK, "登录成功", True)

        except Exception as e:
            return create_response(HTTPStatus.INTERNAL_SERVER_ERROR, f"服务器错误: {str(e)}", False)
