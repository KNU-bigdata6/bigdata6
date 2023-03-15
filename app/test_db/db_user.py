class User():
  def __init__(self, db):
    self.db = db
  
  # 회원가입
  def join(self, user_id, password, name, gender):
    sql = f"insert into userTBL values (NULL, '{user_id}', '{password}', '{name}', '{gender}')"
    conn = self.db.conn
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
  
  # 전체 회원 조회
  def find_all(self):
    pass
  
  # 회원 user_id로 조회
  def find_by_user_id(self, user_id):
    pass