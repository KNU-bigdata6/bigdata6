from db_model.db_connection import USER_DB, conn_db
from db_model.user_query import UserQuery
from flask_login import UserMixin

# 실제 로그인과 기록 조회
class User(UserMixin):
  def __init__(self, id, user_id, password, name, gender):
    self.id = id
    self.user_id = user_id
    self.password = password
    self.name = name
    self.gender = gender
  
  def get_id(self):
    return str(self.id)
  
  # 회원 번호로 조회
  @staticmethod
  def get(id):
    conn_db(USER_DB)
    
    sql = UserQuery.find_by_id(id = id)
    result = USER_DB.select_one(sql)
    
    if not result:
      return None
    else:
      user = User(
        id = result[0],
        user_id  = result[1],
        password = result[2],
        name = result[3],
        gender = result[4]
        )
      return user
  
  # 회원 가입 (중복 검증도 필요)
  @staticmethod
  def join(user_id, password, name, gender):
    # db 연결 x -> 다시 연결
    conn_db(USER_DB)
    
    # 가입 성공유무
    SUCCESS = False
    user = User.find_member(user_id)
    # 해당 유저가 없으면 가입
    if not user:
      sql = UserQuery.save(user_id, password, name, gender)
      USER_DB.execute(sql)
      # 가입 후 다시 조회 유저 정보 넘겨줌
      SUCCESS = True
    return SUCCESS
  
  # 회원 존재 유무 확인 (중복 검증, 회원 조회)
  @staticmethod
  def find_member(user_id):
    # db 연결 x -> 다시 연결
    conn_db(USER_DB)
    
    sql = UserQuery.find_by_user_id(table = 'userTBL', user_id = user_id)
    result = USER_DB.select_one(sql)
    
    if not result:
      return None
    else:
      user = User(
        id = result[0],
        user_id  = result[1],
        password = result[2],
        name = result[3],
        gender = result[4]
        )
      return user
  
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
    
  
  # 회원 기록 조회
  def record():
    pass