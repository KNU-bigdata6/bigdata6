from test_db.database import Database
from test_db.user_query import UserQuery

# 실제 로그인과 기록 조회
class User():
  def __init__(self, id, user_id, password, name, gender):
    self.id = id
    self.user_id = user_id
    self.password = password
    self.name = name
    self.gender = gender
    
  # 회원 가입 (중복 검증도 필요)
  def join():
    pass
  
  # 회원 존재 유무 확인 (중복 검증에 이용)
  def find_member():
    pass
  
  # 회원 기록 조회
  def record():
    pass