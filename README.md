## \# personalWeb

**Develop a personal website using Flask as the backend, Vue+Element Plus as the frontend, MongoDB as the database for storing data**

**接下来我将使用各种前沿的技术在业余的时间去将个人的网站去进行更新，迭代，将各种技术融合起来**

## \# 说明文件

    如果想去在增加新的表以及字段的时候，一定在app.py内进行，其他地方属于未注册区域，例如

```python
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
```

​    

## 接口说明: