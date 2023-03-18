from flask import Flask, render_template, request, jsonify, make_response, Blueprint, redirect, url_for
from service.user import User
import hashlib

L = [["dasfad", "굿"], ["dasfad", "굿"], ["dasfad", "굿"]]

main = Blueprint('main', __name__, url_prefix='/')


@main.route('/')
def vars():
    return render_template('home.html')


@main.route('/test', methods=['GET', 'POST'])
def vars2():
    if request.method == 'POST':
        tdata = request.get_json()
        # 데이터 db넣고 처리한후 ai 응답 담기
        ai = {"data": "굿"}
        L.append([tdata["question"], "굿"])
        # ai db담기
        return jsonify(result="success", result2=ai)
    else:
        # 초기 세팅
        return render_template('test.html')


@main.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        user_id = request.form['userid']
        name = request.form['name']
        password = request.form['password']
        gender = request.form['gender']
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        SUCCESS = User.join(
            user_id=user_id, password=hashed_password, name=name, gender=gender)
        # 가입 실패
        if not SUCCESS:
            return render_template('join.html')
        # 가입 성공
        else:
            return redirect(url_for('main.vars'))
    else:
        return render_template('join.html')
