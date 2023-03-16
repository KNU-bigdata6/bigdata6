from flask import Flask
app = Flask(__name__)
from app.test_db.database import Database
from app.test_db.user_query import UserQuery
from app import routes