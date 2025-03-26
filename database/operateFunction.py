# 下面封装的是我的有关怎么去执行的SQL语句
from flask import jsonify
from config import  CODE_ERROR,CODE_SUCCESS
from database.mongoDB import get_MongoDBConnect
from pymongo.errors import PyMongoError
from otherFunctions.create_response import create_response
class execuFunction():
    def __init__(self):
        # 使用selfClient去进行与数据库去进行连接
        self.client = get_MongoDBConnect()
    # 传入两个数据 dbName 指的是表民 ，insertData指的是存储的数据
    def addData(self, dbName, insertData):
        print(dbName,insertData)
        try:
            result = self.client[dbName].insert_many(insertData)
            return create_response(CODE_SUCCESS, result.inserted_ids)
        except Exception as e:
            return create_response(CODE_ERROR, str(e), success=False)