from flask import Flask, render_template, request, jsonify, make_response, Blueprint, redirect, url_for
from service.user import User
import hashlib

L = [["dasfad", "굿"], ["dasfad", "굿"], ["dasfad", "굿"]]

main = Blueprint('login', __name__, url_prefix='/login')