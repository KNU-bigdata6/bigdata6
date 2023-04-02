from flask import Flask, render_template, request, jsonify, make_response, Blueprint, redirect, url_for, flash
from flask_login import current_user
from service.user import User
import speech_recognition as sr
from gtts import gTTS
import base64
import json
import os


chat = Blueprint('chat', __name__, url_prefix='/test')

# 텍스트 대화처리
@chat.route('/<subject>', methods=['GET', 'POST'])
def text(subject):
    if current_user.is_authenticated:
        if request.method == 'POST':
            tdata = request.get_json()
            question = tdata['question']

            # 답변 생성
            answer = "request"
            answer_to_voice = gTTS(text=answer, lang="en")
            c_user_id = current_user.get_user_id()
            answer_to_voice.save(f"./audio/{c_user_id}_{answer}.mp3")
            with open(f"./audio/{c_user_id}_{answer}.mp3", "rb") as audio_file:
                audio_binary = audio_file.read()
                encoded_string = base64.b64encode(audio_binary)
            os.remove(f"./audio/{c_user_id}_{answer}.mp3")
            ai = {"data": answer, "answer_audio": encoded_string.decode()}

            # 답변 DB저장
            User.record(current_user.user_id,  question, answer)
            # ai db담기
            return jsonify(result="success", result2=ai)
        else:
            return render_template(f'{subject}.html', login=True)
    else:
        # 경고문 띄우기
        flash("not login")
        return redirect(url_for('main.login'))


# 음성 대화처리
@chat.route('/<subject>/audio', methods=['GET', 'POST'])
def audio(subject):
    if request.method == 'POST' and current_user.is_authenticated:
        result = sr.AudioFile(request.files['audio'])

        r = sr.Recognizer()
        with result as source:
            audio = r.listen(source)
        try:
            # 텍스트 처리 stt, 추후 영어로 변경
            question = r.recognize_google(audio, language='en')
            # 답변 생성
            answer = "request"
            answer_to_voice = gTTS(text=answer, lang="en")
            c_user_id = current_user.get_user_id()
            answer_to_voice.save(f"./audio/{c_user_id}_{answer}.mp3")

            with open(f"./audio/{c_user_id}_{answer}.mp3", "rb") as audio_file:
                audio_binary = audio_file.read()
                encoded_string = base64.b64encode(audio_binary)
            os.remove(f"./audio/{c_user_id}_{answer}.mp3")

            ai = {"data": answer, "request": question,
                "answer_audio": encoded_string.decode()}
            print(encoded_string.decode())

            # 답변 전송
            User.record(current_user.user_id, question, answer)

            return jsonify(result="success", result2=ai)

        except sr.UnknownValueError:
            print("Google 음성 인식이 오디오를 이해할 수 없습니다.")
            ai = {"data": "Google 음성 인식이 오디오를 이해할 수 없습니다."}
            return jsonify(result="success", result2=ai)
        except sr.RequestError as e:
            print("Google 음성 인식 서비스에서 결과를 요청할 수 없습니다.; {0}".format(e))
            ai = {"data": "Google 음성 인식 서비스에서 결과를 요청할 수 없습니다."}
            return jsonify(result="success", result2=ai)