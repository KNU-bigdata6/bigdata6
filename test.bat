@echo off 

IF NOT EXIST venv (
  python -m venv venv
  actiavte venv
  pip install --upgrade pip
  pip install -r requirements.txt
)

activate venv
SET FLASK_APP = runserver.py
Flask run