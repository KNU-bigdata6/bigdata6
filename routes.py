from flask import Flask, render_template, request, jsonify, make_response, Blueprint, redirect, url_for
from flask_login import login_user, logout_user, current_user
from service.user import User
import hashlib

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/')
def vars():
    # runserver의 user_loader가 호출됨 flask login이 http request에서 id를 자동으로 넣어줌
    if current_user.is_authenticated:
        print("로그인된 사용자")
        print(current_user.name)
    else:
        print("안돼 돌아가")
    return render_template('home.html')


@main.route('/test', methods=['GET', 'POST'])
def vars2():
    if request.method == 'POST':
        tdata = request.get_json()
        # 데이터 db넣고 처리한후 ai 응답 담기
        ai = {"data": "굿"}
        # ai db담기
        return jsonify(result="success", result2=ai)
    else:
        # 초기 세팅
        return render_template('test.html')

@main.route('/join', methods = ['GET','POST'])
def join():
    if request.method == 'POST':
        user_id = request.form['userid']
        name = request.form['name']
        password = request.form['password']
        gender = "남" if request.form['gender'] == 'Male' else "여"
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        
        SUCCESS = User.join(user_id = user_id , password = hashed_password, name = name, gender = gender)
        # 가입 실패
        if not SUCCESS:
            return render_template('join.html')
        # 가입 성공
        else:
            return redirect(url_for('main.vars'))
    else:
        return render_template('join.html')


@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['userid']
        password = request.form['password']
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        
        user = User.user_check(user_id, hashed_password)
        # 아이디나 비밀번호가 틀린 경우
        if not user :
            return render_template('login.html')
        else:
            print(user.user_id, user.password, user.name, user.gender)
            login_user(user)
            return redirect(url_for('main.vars'))
    else:
        return render_template('login.html')

# GET 메소드는 임시로 logout 버튼이 없어서 만들어 놓은것
@main.route('/logout', methods = ['GET','POST'])
def logout():
    logout_user()
    return redirect(url_for('main.vars'))
