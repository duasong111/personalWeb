from functions.secureCheck import verifyPassword
from otherFunctions.create_response import create_response
from flask import Flask, request, jsonify, Response
import secrets
from datetime import datetime, timedelta
from database.operateFunction import execuFunction
import bcrypt
from http import HTTPStatus
# 检查用户是否登录成功的函数
class LoginFunction:
    def checklogin(self, username=None, password=None):
        try:
            # 1. 验证输入
            if not username or not password:
                return create_response(HTTPStatus.BAD_REQUEST, "用户名和密码为必填项", False)
            # 2. 查询用户
            db_function = execuFunction()
            query_result = db_function.query_individual_users(
                dbName='users',
                queryParams="username",
                queryData=username)
            # 3. 检查用户是否存在
            if not query_result:
                return create_response(HTTPStatus.BAD_REQUEST, "用户名或密码错误", False)
            # 4. 验证密码
            stored_password = query_result['password']  # 数据库中的哈希值
            stored_salt = bytes.fromhex(query_result['salt'])  # 数据库中的盐值（十六进制转字节）
            if not verifyPassword(password, stored_password, stored_salt):
                return create_response(HTTPStatus.BAD_REQUEST, "用户名或密码错误", False)
            # 5. 生成 token
            new_token = secrets.token_hex(16)  # 32 字符的随机 token
            # 6. 更新数据库中的 token 和 lastLogin
            update_result = db_function.update_user_key_value(
                db_name='users',
                username=username,
                key_value='username',
                new_data=new_token,
                key_type='token')
            # 更新 lastLogin
            update_time_result = db_function.update_user_key_value(
                db_name='users',
                username=username,
                key_value='username',
                new_data=datetime.now(),
                key_type='lastLogin')
            if not update_time_result.get('success', False):
                return create_response(HTTPStatus.INTERNAL_SERVER_ERROR, "无法更新时间节点", False)
            if not update_result.get('success', False):
                return create_response(HTTPStatus.INTERNAL_SERVER_ERROR, "无法更新用户 token", False)
            # 8. 返回成功响应，包含 token
            return create_response(
                HTTPStatus.OK,
                "登录成功",
                True,
                data={"token": new_token})
        except ValueError as ve:
            return create_response(HTTPStatus.BAD_REQUEST, f"输入错误: {str(ve)}", False)
        except Exception as e:
            return create_response(HTTPStatus.INTERNAL_SERVER_ERROR, f"服务器错误: {str(e)}", False)