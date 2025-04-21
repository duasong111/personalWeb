# 该文件是去了将连接数据库暴露出去

from pymongo import MongoClient
from config import MONGO_URI, MONGO_DB
def get_MongoDBConnect():
    client = MongoClient(MONGO_URI)
    mongoConnect = client[MONGO_DB]
    return mongoConnect
