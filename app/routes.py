from flask import Flask, render_template, request, jsonify
from app import app
L = [["dasfad", "굿"], ["dasfad", "굿"], ["dasfad", "굿"]]


@app.route('/')
def vars():
    return render_template('home.html')


@app.route('/test', methods=['GET', 'POST'])
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
        return render_template('test.html', data_list=L)
