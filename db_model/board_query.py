class BoardQuery():
  # 게시물 저장 코드(아이디, 회원 아이디, 제목, 내용, 작성자, 지역, 구군, 날짜)
  @staticmethod
  def save(id, user_id, title, content, name, city, district, date):
    sql = f"INSERT INTO postTBL VALUES (NULL, '{id}', '{user_id}', '{title}', '{content}', '{name}', '{city}', '{district}', 0,  '{date}')"
    return sql
  
  # 게시물 전체 조회 코드
  @staticmethod
  def find_all():
    sql = f"SELECT * FROM postTBL"
    return sql
  
  @staticmethod
  def increase_one(index):
    sql = f"UPDATE postTBL SET views = views + 1 WHERE idx = {index}"
    return sql