from flask import Flask, request
from test_db.database import Database
from test_db.db_user import User

app = Flask(__name__)

'''
실행 예시
db = Database(host='localhost', port = 3306, user = 'root', password = '1234', db_name = 'test_userDB')
db.connect()

user = User(db)
user.join(user_id = 'fm2020', password = '1234', name = '김철수', gender = "여")
'''