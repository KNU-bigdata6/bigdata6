from flask import Flask, render_template, request, jsonify, make_response
from app import app
from app import Database
from app import UserQuery
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


@app.route('/test_db')
def test_db():
    '''
        DB 관련 코드 예제
    '''
    
    # db 연결
    db = Database(host='localhost', port = 3306, user = 'root', password = '1234', db_name = 'test_userDB')
    db.connect()
    # 회원저장
    sql = UserQuery.save(user_id = 'fm22', password = '1234', name = '김철수', gender = "남")
    db.execute(sql)
    
    # # 회원 1명 조회
    sql = UserQuery.find_by_user_id(user_id = 'fm2020', table = "userTBL")
    result = db.select_one(sql)
    print(result)
    
    # 전체 회원 조회 (튜플 형식으로 가져옴)
    sql = UserQuery.find_all(table = "userTBL")
    result_list = db.select_all(sql)
    print(result_list)
    
    return make_response('200', 200)