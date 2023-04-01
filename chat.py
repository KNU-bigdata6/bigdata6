from flask import Flask, render_template, request, jsonify, make_response, Blueprint, redirect, url_for, flash
from flask_login import current_user
from service.user import User
import speech_recognition as sr


chat = Blueprint('chat', __name__, url_prefix='/test')


@chat.route('/business', methods=['GET', 'POST'])
def business():
    if current_user.is_authenticated:
        if request.method == 'POST':
            tdata = request.get_json()
            # 데이터 db넣고 처리한후 ai 응답 담기
            User.record(current_user.user_id, tdata['question'], "굿")
            ai = {"data": "굿"}
            # ai db담기
            return jsonify(result="success", result2=ai)
        else:
            return render_template('business.html', userid=current_user.user_id, login=True)
    else:
        # 경고문 띄우기
        flash("not login")
        return redirect(url_for('main.login'))


@chat.route('/business/audio', methods=['GET', 'POST'])
def audio():
    if request.method == 'POST':
        result = sr.AudioFile(request.files['audio'])

        r = sr.Recognizer()
        with result as source:
            audio = r.listen(source)
        try:
            # 텍스트 처리 stt
            question = r.recognize_google(audio, language='ko')
            print(question)
            
            # 답변 생성
            answer = "답변"
            
            # 답변 전송
            User.record(current_user.user_id, question, answer)
            ai = {"data": answer}
            return jsonify(result="success", result2=ai)

        except sr.UnknownValueError:
            print("Google 음성 인식이 오디오를 이해할 수 없습니다.")
            ai = {"data": "Google 음성 인식이 오디오를 이해할 수 없습니다."}
            return jsonify(result="success", result2=ai)
        except sr.RequestError as e:
            print("Google 음성 인식 서비스에서 결과를 요청할 수 없습니다.; {0}".format(e))
            ai = {"data": "Google 음성 인식 서비스에서 결과를 요청할 수 없습니다."}
            return jsonify(result="success", result2=ai)


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
            return render_template('study.html', userid=current_user.user_id, login=True)
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
            return render_template('life.html', userid=current_user.user_id, login=True)
    else:
        # 경고문 띄우기
        flash("not login")
        return redirect(url_for('main.login'))
