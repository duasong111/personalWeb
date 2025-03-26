# 该文件为测试文件用来测试数据库是否能够进行连接

from operateFunction  import execuFunction

if __name__ == '__main__':

    # 插入输入测试
    data = {
    "tableName": "users",
    "insertList": [
        {
            "student_id": "2023008",
            "name": "张八嘎",
            "age": 18,
            "grade": "高三",
            "class": "三班",
            "contact_phone": "138-0000-0001"
        }
    ]
}
    print(data["tableName"],'--------------',data['insertList'])

    print(execuFunction().addData(dbName=data["tableName"],insertData=data["insertList"]))