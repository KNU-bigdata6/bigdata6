from db_model.db_connection import USER_DB, conn_db
from db_model.user_query import UserQuery
from db_model.record_query import RecordQuery
from flask_login import UserMixin
from datetime import datetime


# user 관련 객체 생성 (회원 번호 조회, 회원 가입, 회원 존재 유무, 회원 탈퇴, login id pw 검증, 회원 대화 기록 저장)
class User(UserMixin):
    def __init__(self, id, user_id, password, name, gender):
        self.id = id
        self.user_id = user_id
        self.password = password
        self.name = name
        self.gender = gender

    def get_id(self):
        return str(self.id)
    
    def get_user_id(self):
        return str(self.user_id)
    
    def get_user_info(self):
        user = [self.user_id , self.name , self.gender]
        return user

    # 회원 번호로 조회
    @staticmethod
    def get(id):
        conn_db(USER_DB)

        sql = UserQuery.find_by_id(id=id)
        result = USER_DB.select_one(sql)

        if not result:
            return None
        else:
            user = User(
                id=result[0],
                user_id=result[1],
                password=result[2],
                name=result[3],
                gender=result[4]
            )
            return user

    # 회원 가입 (중복 검증도 필요)
    @staticmethod
    def join(user_id, password, name, gender):
        # db 연결 x -> 다시 연결
        conn_db(USER_DB)
        sql = UserQuery.save(user_id, password, name, gender)
        USER_DB.execute(sql)
        # 가입 후 다시 조회 유저 정보 넘겨줌
        SUCCESS = True
        return SUCCESS

    @staticmethod
    def check(user_id):
        conn_db(USER_DB)
        SUCCESS = False
        user = User.find_member(user_id)
        # 해당 유저가 없으면 성공
        if not user:
            SUCCESS = True
        return SUCCESS


    # 회원 존재 유무 확인 (중복 검증, 회원 조회)
    @staticmethod
    def find_member(user_id):
        # db 연결 x -> 다시 연결
        conn_db(USER_DB)

        sql = UserQuery.find_by_user_id(user_id=user_id)
        result = USER_DB.select_one(sql)

        if not result:
            return None
        else:
            user = User(
                id=result[0],
                user_id=result[1],
                password=result[2],
                name=result[3],
                gender=result[4]
            )
            return user

    # 회원 탈퇴 
    @staticmethod
    def withdrawal(id):
        conn_db(USER_DB)

        sql = UserQuery.delete_by_id(id = id)
        USER_DB.execute(sql)
        
        SUCCESS = True
        return SUCCESS


    # login 할때 id, pw 체크
    @staticmethod
    def user_check(user_id, password):
        # 해당 유저 아이디의 사용자 조회
        user = User.find_member(user_id)

        # 해당 유저 아이디의 사용자가 없는 경우
        if not user or user.password != password:
            return None
        # 비밀번호가 일치하는 경우
        else:
            return user

    # password 변경 (아직 사용 X)
    @staticmethod
    def user_password_change(id, new_password):
        sql = UserQuery.update_password_by_id(id, new_password)
        USER_DB.execute(sql)
        
        SUCCESS = True
        return SUCCESS
    
    # 회원 대화 기록 저장
    @staticmethod
    def record(subject, user_id, question, answer):
        conn_db(USER_DB)

        # 회원 번호 조회
        user = User.find_member(user_id)
        id = user.id
        sql = RecordQuery.save(id, subject, question, answer,
                            datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        USER_DB.execute(sql)
    
