class RecordQuery():
  # 대화 기록 저장
  @staticmethod
  def save(id, question, answer, date):
    sql = f"INSERT INTO userTBL VALUES ({id}, '{question}', '{answer}', '{date}')"
    return sql
  
  # 시간에 따라 삭제 (일단은 특정 시간에 삭제하는 구문)
  @staticmethod
  def delete_by_date(date):
    sql = f"DELETE FROM userTBL WHERE date = '{date}'"
    return sql
