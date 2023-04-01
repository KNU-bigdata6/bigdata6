class UserQuery():
  # 회원저장 쿼리
  @staticmethod
  def save(user_id, password, name, gender):
    sql = f"INSERT INTO userTBL VALUES (NULL, '{user_id}', '{password}', '{name}', '{gender}')"
    return sql
  
  # 전체 회원 조회 쿼리
  @staticmethod
  def find_all():
    sql = f"SELECT * FROM userTBL"
    return sql
  
  # 회원 user_id로 조회 쿼리
  @staticmethod
  def find_by_user_id(user_id):
    sql = f"SELECT * FROM userTBL WHERE userid = '{user_id}'"
    return sql
  
  # 회원 번호로 조회 쿼리
  @staticmethod
  def find_by_id(id):
    sql = f"SELECT * FROM userTBL WHERE id  = {id}"
    return sql
  
  # 회원 삭제 쿼리
  @staticmethod
  def delete_by_id(id):
    sql = f"DELETE FROM userTBL WHERE id = {id}"
    return sql
  
  # 회원 비밀 번호 수정 쿼리
  @staticmethod
  def update_password_by_id(id, new_password):
    sql = f"UPDATE userTBL SET password = '{new_password}' WHERE id = {id}"
    return sql
