from flask import Flask, render_template, request, jsonify, make_response, Blueprint, redirect, url_for, flash
from flask_login import current_user
from service.user import User

chat = Blueprint('chat', __name__, url_prefix='/test')


@chat.route('/businesse', methods=['GET', 'POST'])
def bussniese():
    if current_user.is_authenticated:
        if request.method == 'POST':
            tdata = request.get_json()
            # 데이터 db넣고 처리한후 ai 응답 담기
            User.record(current_user.user_id, tdata['question'], "굿")
            ai = {"data": "굿"}
            # ai db담기
            return jsonify(result="success", result2=ai)
        else:
            return render_template('test.html', userid=current_user.user_id, login=True)
    else:
        # 경고문 띄우기
        flash("not login")
        return redirect(url_for('main.login'))


@chat.route('/study', methods=['GET', 'POST'])
def study():
    if current_user.is_authenticated:
        if request.method == 'POST':
            tdata = request.get_json()
            # 데이터 db넣고 처리한후 ai 응답 담기
            User.record(current_user.user_id, tdata['question'], "굿")
            ai = {"data": "굿"}
            # ai db담기
            return jsonify(result="success", result2=ai)
        else:
            return render_template('test.html', userid=current_user.user_id, login=True)
    else:
        # 경고문 띄우기
        flash("not login")
        return redirect(url_for('main.login'))


@chat.route('/life', methods=['GET', 'POST'])
def life():
    if current_user.is_authenticated:
        if request.method == 'POST':
            tdata = request.get_json()
            # 데이터 db넣고 처리한후 ai 응답 담기
            User.record(current_user.user_id, tdata['question'], "굿")
            ai = {"data": "굿"}
            # ai db담기
            return jsonify(result="success", result2=ai)
        else:
            return render_template('test.html', userid=current_user.user_id, login=True)
    else:
        # 경고문 띄우기
        flash("not login")
        return redirect(url_for('main.login'))