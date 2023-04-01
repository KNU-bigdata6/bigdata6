from flask import Flask, render_template, request, jsonify, make_response, Blueprint, redirect, url_for, flash
from flask_login import current_user, logout_user
from service.user import User
import hashlib

info = Blueprint('myinfo', __name__, url_prefix='/myinfo')


# 내 정보 페이지 (회원 탈퇴, password 수정 구현)
@info.route('/')
def myinfo():
    print(current_user.id)
    return render_template('myinfo.html')


# 회원탈퇴 관련
@info.route('/withdrawal', methods=['POST'])
def withdrwal():
    # SUCCESS : 성공 여부
    SUCCESS = User.withdrawal(id = current_user.id)
    
    # 로그아웃
    logout_user()
    
    # 성공 여부 보내고 다시 메인 페이지로
    return redirect(url_for('main.home'))


# password 수정 구현
@info.route('/newpassword', methods=['POST'])
def newpassword():
    # 새로 입력한 패스워드 post로 받아옴
    new_password = request.form['new_password']
    
    hashed_password = hashlib.sha256(new_password.encode('utf-8')).hexdigest()
    
    # SUCCESS : 성공 여부
    SUCCESS = User.user_password_change(current_user.id, hashed_password)
    
    # 로그아웃
    logout_user()
    
    # 성공 여부 보내고 다시 내정보 페이지로
    return redirect(url_for('main.login'))