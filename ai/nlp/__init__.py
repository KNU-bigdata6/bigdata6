from flask import Flask
from transformers import AutoModelWithLMHead, AutoModelForCausalLM, AutoTokenizer
import torch
from .routes.business_dialogue import business
from .routes.daily_dialogue import daily
from flask_cors import CORS
from .routes.hospital_dialogue import hospital

def create_app():

    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(business)
    app.register_blueprint(daily)
    app.register_blueprint(hospital)
    return app

app = create_app()
