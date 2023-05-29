from db_model.database import Database

USER_DB =  Database(
  host='localhost',
  port = 3306,
  user = 'root',
  password = '1234',
  db_name = 'test_userDB'
  )

def conn_db(db : Database):
  # mysql 연결이 끊어져 있으면
  if not db.conn:
    db.connect()