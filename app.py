from bson import ObjectId

from database.test import ISODate
from otherFunctions.create_response import create_response
from flask import Flask, request, jsonify, Response
from functions.userLogin import LoginFunction
from database.operateFunction import execuFunction
from flask_cors import CORS
import bcrypt
from http import HTTPStatus
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
checkLogin = LoginFunction()
db_function = execuFunction()

# 实现用户的登录功能
@app.route("/login", methods=["POST"],strict_slashes=False)
def login():
    try:
        data = request.get_json()  # 解析 JSON 数据
        user = data.get('username')
        pwd = data.get('password')
        return checkLogin.checklogin(user,pwd)
    except Exception as e:
        return create_response(HTTPStatus.INTERNAL_SERVER_ERROR, f"服务器错误: {str(e)}", False)
# 可以去自定义的去控制首界面的饼图
@app.route("/get_pie_value", methods=["GET"])
def define_pie():
    try:
        pass
    except Exception as e:
        return create_response(HTTPStatus.INTERNAL_SERVER_ERROR, f"服务器错误: {str(e)}", False)


# 通过这个区进行添加表
@app.route("/add_table",methods=["GET"])
def add_table():
    data = {
        "tableName": "skill_manage",
        "insertList": [
            {
                "value": 1000,
                "name": "Python后端",
                "title": "Django Flask FastApi + 爬虫",
                "memo": "备注信息",
                "createdAt": ISODate("2025-03-26T10:00:00Z"),
                "updatedAt": ISODate("2025-03-26T12:00:00Z"),
            }
        ]
    }
    print(execuFunction().add_data(dbName=data["tableName"], insertData=data["insertList"]))
    return "sucess"

# 写一个自动获取github和gitee更新数量的脚本，然后能够不断地去展现出来数据



if __name__ == '__main__':
    app.run()
