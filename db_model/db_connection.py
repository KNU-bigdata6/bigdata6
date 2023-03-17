from db_model.database import Database

USER_DB =  Database(
  host='localhost',
  port = 3306,
  user = 'root',
  password = '1234',
  db_name = 'test_userDB'
  )

if USER_DB.conn == None:
  USER_DB.connect()