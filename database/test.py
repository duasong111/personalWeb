# 该文件为测试文件用来测试数据库是否能够进行连接
import secrets

from bson import ObjectId
from datetime import datetime
from database.operateFunction import execuFunction
from database.operateFunction import execuFunction as dbFunction
import hashlib
# 用户的密码使用md5进行加密
def ISODate(param):
    if param:
        # 如果提供了参数，尝试将其解析为 datetime 对象
        try:
            return datetime.fromisoformat(param.replace("Z", "+00:00"))
        except ValueError as e:
            raise ValueError(f"无效的日期格式: {param}, 请使用 ISO 8601 格式，例如 '2025-03-26T10:00:00Z'")
    else:
        # 如果未提供参数，返回当前时间的 datetime 对象
        return datetime.utcnow()

def queryData():
    dbDate = execuFunction()
    queryResult = dbDate.query_individual_users(dbName='users', queryParams="username", queryData="duasong")
    return queryResult
def updateDate():
    dbDate = execuFunction()
    new_token = secrets.token_hex(16)
    queryResult = dbDate.update_user_token(dbName='users', username="duasong", new_token=new_token)
    return queryResult


if __name__ == '__main__':
    # result = queryData()
    # print(result)

    # 插入输入测试
#     data = {
#     "tableName": "users",
#     "insertList": [
#         {
#             "_id": ObjectId("605c72ef9f1b2c001f8b4567"),
#             "username": "blogger123",
#             # "token":"434342frcse",
#             "email": "blogger123@example.com",
#             "password": "$2b$10$hashedPasswordHere",
#             "fullName": "张三",
#             "salt": "b6326d2a69d00a69d6b7037197db3d6f",
#             "profilePicture": "https://example.com/images/blogger123.jpg",
#             "bio": "热爱写作的技术博主",
#             "role": "user",
#             "isVerified": True,
#             "createdAt": ISODate("2025-03-26T10:00:00Z"),
#             "updatedAt": ISODate("2025-03-26T12:00:00Z"),
#             "lastLogin": ISODate("2025-03-26T12:00:00Z"),
#             "socialLinks": {
#                 "CSDN": "https://twitter.com/blogger123",
#                 "github": "https://github.com/blogger123",
#                 "gitee": "https://github.com/blogger123"
#             },
#             "preferences": {
#                 "theme": "light",
#                 "notifications": True
#             },
#         }
#     ]
# }

    data = {
        "tableName":"skill_manage",
        "insertList":[
            {
             "value": 1000,
             "name" : "Python后端",
             "title" : "Django Flask FastApi + 爬虫",
             "memo" : "备注信息",
             "createdAt" : ISODate("2025-03-26T10:00:00Z"),
              "updatedAt": ISODate("2025-03-26T12:00:00Z"),
            }
        ]
    }
    # print(data["tableName"],'--------------',data['insertList'])
# #
    print(execuFunction().add_data(dbName=data["tableName"],insertData=data["insertList"]))