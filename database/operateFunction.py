# 下面封装的是我的有关怎么去执行的SQL语句
from flask import jsonify
from datetime import datetime
from config import  CODE_ERROR,CODE_SUCCESS
from database.mongoDB import get_MongoDBConnect
from pymongo.errors import PyMongoError
from otherFunctions.create_response import create_response
class execuFunction():
    def __init__(self):
        # 使用selfClient去进行与数据库去进行连接
        self.client = get_MongoDBConnect()
    # 传入两个数据 dbName 指的是表民 ，insertData指的是存储的数据
    def add_data(self, dbName, insertData):
        try:
            result = self.client[dbName].insert_many(insertData)
                                                           # 最后一个参数存在问题
            return create_response(CODE_SUCCESS, result.inserted_ids,CODE_SUCCESS)
        except Exception as e:
            return create_response(CODE_ERROR, str(e), success=False)
    # 执行查询单个查询验证命令
    def query_individual_users(self, dbName,queryParams, queryData):
        try:
            return self.client[dbName].find_one({queryParams: queryData})
        except Exception as e:
            return create_response(CODE_ERROR, str(e), success=False)
    # 更新单个数据所使用的集成接口
    def update_user_key_value(self, db_name, key_value, username, new_data, key_type):
        try:
            # 检查 key_value 和 key_type 是否有效
            if not key_value or not key_type:
                return {"success": False, "message": "key_value 和 key_type 不能为空"}
            # 处理 datetime 类型的输入，确保它可以在 MongoDB 中正确保存
            if isinstance(new_data, datetime):
                new_data = new_data.isoformat()  # 转换为 ISO 格式字符串
            elif isinstance(new_data, str) and new_data.lower() == "now":
                new_data = datetime.now().isoformat()  # 如果传入 "now"，将其转换为当前时间
            # 执行数据库操作
            result = self.client[db_name].update_one(
                {key_value: username},  # 使用用户名作为查询条件
                {"$set": {key_type: new_data}}
            )
            return {
                "success": result.matched_count > 0,
                "message": f"{key_type} 更新成功" if result.matched_count > 0 else f"未找到用户 {username}"
            }
        except Exception as e:
            return {"success": False, "message": f"更新失败: {str(e)}"}






