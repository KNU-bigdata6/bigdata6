from flask import Flask, render_template, request, jsonify, make_response, Blueprint, redirect, url_for, flash
from flask_login import current_user, logout_user
from service.user import User
import hashlib

info = Blueprint('info', __name__, url_prefix='/myinfo')


# 내 정보 페이지 (회원 탈퇴, password 수정 구현)
@info.route('/', methods=['GET', 'POST'])
def myinfo():
    if current_user.is_authenticated:
        user = current_user.get_user_info()
        return render_template('myinfo.html', login=True, user=user)
    else:
        return render_template('login.html')


# 회원탈퇴 관련
@info.route('/withdrawal', methods=['POST', 'GET'])
def withdrawal():
    if request.method == 'POST':
        user_id = current_user.get_user_id()
        password = request.form['password']
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        user = User.user_check(user_id, hashed_password)
        # 아이디나 비밀번호가 틀린 경우
        if not user:
            flash("password is different")
            return render_template('delete.html', login=True)
        else:
            # SUCCESS : 성공 여부
            SUCCESS = User.withdrawal(id=current_user.id)
            # 로그아웃
            logout_user()
            # 성공 여부 보내고 다시 메인 페이지로
            return redirect(url_for('main.home'))
    else:
        if current_user.is_authenticated:
            return render_template('delete.html', login=True)
        else:
            return render_template('login.html')


# password 수정 구현
@info.route('/newpassword', methods=['POST'])
def newpassword():
    if request.method == 'POST':
        user_id = current_user.get_user_id()
        current_password = request.form['password1']
        hashed_password = hashlib.sha256(
            current_password.encode('utf-8')).hexdigest()

        user = User.user_check(user_id, hashed_password)
        # 아이디나 비밀번호가 틀린 경우
        if not user:
            # 경고문 띄우기
            flash("current password is different")
            user = current_user.get_user_info()
            return render_template('myinfo.html', login=True, user=user)
        else:
            new_password = request.form['password2']
            hashed_password = hashlib.sha256(
                new_password.encode('utf-8')).hexdigest()
            # SUCCESS : 성공 여부
            SUCCESS = User.user_password_change(
                current_user.id, hashed_password)
            print(SUCCESS)
            # 로그아웃
            logout_user()
            # 성공 여부 보내고 다시 내정보 페이지로
            return redirect(url_for('main.login'))
