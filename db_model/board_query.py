class BoardQuery():
  # 게시물 저장 쿼리(아이디, 회원 아이디, 제목, 내용, 작성자, 지역, 구군, 날짜)
  @staticmethod
  def save(id, user_id, title, content, name, city, district, date):
    sql = f"INSERT INTO postTBL VALUES (NULL, '{id}', '{user_id}', '{title}', '{content}', '{name}', '{city}', '{district}', 0,  '{date}')"
    return sql
  
  # 게시물 전체 조회 쿼리
  @staticmethod
  def find_all():
    sql = f"""SELECT postTBL.*,
              COUNT(commentTBL.comment_num) AS comment_count
              FROM postTBL
              LEFT JOIN commentTBL ON postTBL.idx = commentTBL.idx
              GROUP BY postTBL.idx"""
    return sql
  
  # 게시물 검색 조회 쿼리
  @staticmethod
  def find_all_by_category(category, query):
    sql = f"""SELECT postTBL.*,
              COUNT(commentTBL.comment_num) AS comment_count
              FROM postTBL
              LEFT JOIN commentTBL ON postTBL.idx = commentTBL.idx
              WHERE {category} LIKE '%{query}%'
              GROUP BY postTBL.idx"""
    return sql
  
  # 게시글 위치 조회 커리
  @staticmethod
  def find_all_by_location(city, district):
    sql = f"""SELECT postTBL.*,
              COUNT(commentTBL.comment_num) AS comment_count
              FROM postTBL
              LEFT JOIN commentTBL ON postTBL.idx = commentTBL.idx
              WHERE city = '{city}' AND district = '{district}'
              GROUP BY postTBL.idx"""
    return sql
  
  # 게시글 글 번호로 조회 쿼리
  @staticmethod
  def find_by_index(index):
    sql = f"SELECT * FROM postTBL WHERE idx = {index}"
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
  
  # 댓글 조회 쿼리
  @staticmethod
  def find_comment_by_index(index):
    sql = f"SELECT * FROM commentTBL WHERE idx = {index}"
    return sql


  # 댓글 등록 쿼리
  @staticmethod
  def save_comment(index, id, user_id, text, name, date):
    sql = f"INSERT INTO commentTBL VALUES (NULL, {index}, '{id}', '{user_id}', '{text}', '{name}', '{date}')"
    return sql
  
  # 게시글 삭제 쿼리
  @staticmethod 
  def delete_by_comment_num(comment_num, index):
    print(comment_num, index)
    sql = f"DELETE FROM commentTBL WHERE comment_num = {comment_num} AND idx = {index}"
    return sql
  


