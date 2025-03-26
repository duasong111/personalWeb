from flask import Flask,jsonify,request
from pymongo import MongoClient
from database.operateFunction import execuFunction

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # 获取请求数据（假设是 JSON 格式）
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    return "11111111111"

@app.route('/insertData', methods=['POST'])
def insert_data():
    data = request.get_json()
    print(data.get('tableName'),'------------',data.get('insertList'))
    result = execuFunction().addData(dbName=data.get('tableName'), insertData=data.get('insertList'))
    return jsonify({'status': 'success', 'message': '数据已插入！', 'result': result}), 200

if __name__ == '__main__':
    app.run()
