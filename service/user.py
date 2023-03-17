from db_model.db_connection import USER_DB
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
  
  # 회원 가입 (중복 검증도 필요)
  @staticmethod
  def join(user_id, password, name, gender):
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
  
  # 회원 기록 조회
  def record():
    pass