class BoardQuery():
  # 게시물 저장 쿼리(아이디, 회원 아이디, 제목, 내용, 작성자, 지역, 구군, 날짜)
  @staticmethod
  def save(id, user_id, title, content, name, city, district, date):
    sql = f"INSERT INTO postTBL VALUES (NULL, '{id}', '{user_id}', '{title}', '{content}', '{name}', '{city}', '{district}', 0,  '{date}')"
    return sql
  
  # 게시물 전체 조회 쿼리
  @staticmethod
  def find_all():
    sql = f"SELECT * FROM postTBL"
    return sql
  
  # 게시물 전체 조회 쿼리
  @staticmethod
  def find_all_by_name(query):
    sql = f"SELECT * FROM postTBL WHERE name LIKE '%{query}%'"
    return sql
  
  # 게시물 전체 조회 쿼리
  @staticmethod
  def find_all_by_title(query):
    sql = f"SELECT * FROM postTBL WHERE title LIKE '%{query}%'"
    return sql
  
  # 게시물 전체 조회 쿼리
  @staticmethod
  def find_all_by_userid(query):
    sql = f"SELECT * FROM postTBL WHERE userid LIKE '%{query}%'"
    return sql
  
  # 게시글 글 번호로 조회 쿼리
  @staticmethod
  def find_by_index(index):
    sql = f"SELECT * FROM postTBL WHERE idx = '{index}'"
    return sql

  # 게시글 삭제 
  @staticmethod
  def delete_by_index(index):
    sql = f"DELETE FROM postTBL WHERE idx = '{index}'"
    return sql
  
    # 회원 비밀 번호 수정 쿼리
  @staticmethod
  def update_password_by_id(id, new_password):
    sql = f"UPDATE userTBL SET password = '{new_password}' WHERE id = {id}"
    return sql

  # 게시글 수정 쿼리
  @staticmethod
  def full_post_update(index, title, content, city, district, date):
    sql = f"UPDATE postTBL SET title = '{title}', content = '{content}', city = '{city}', district = '{district}', date = '{date}' WHERE idx = {index}"
    return sql
  
  # 게시글 조회수 증가 쿼리
  @staticmethod
  def increase_one(index):
    sql = f"UPDATE postTBL SET views = views + 1 WHERE idx = {index}"
    return sql
  


