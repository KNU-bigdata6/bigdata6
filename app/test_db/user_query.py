class UserQuery():
  # 회원저장 쿼리
  @staticmethod
  def save(user_id, password, name, gender):
    sql = f"INSERT INTO userTBL VALUES (NULL, '{user_id}', '{password}', '{name}', '{gender}')"
    return sql
  
  # 전체 회원 조회 쿼리
  @staticmethod
  def find_all(table):
    sql = f"SELECT * FROM {table}"
    return sql
  
  # 회원 user_id로 조회 쿼리
  @staticmethod
  def find_by_user_id(table, user_id):
    sql = f"SELECT * FROM {table} WHERE userid = '{user_id}'"
    return sql
  
  # 회원 탈퇴 쿼리
  @staticmethod
  def withdrawl(table, user_id):
    sql = f"DELETE FROM {table} WHERE userid = '{user_id}'"
    return sql
