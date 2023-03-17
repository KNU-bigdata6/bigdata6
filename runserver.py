from flask import Flask
from routes import main

app = Flask(__name__)

app.register_blueprint(main)
