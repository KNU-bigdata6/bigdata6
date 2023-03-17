import pymysql

class Database:
    def __init__(self, host, port, user, password, db_name, charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.charset = charset
        self.db_name = db_name
        self.conn = None

    # DB 연결
    def connect(self):
        if self.conn != None:
            return

        self.conn = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            db = self.db_name,
            charset = self.charset
        )

    # DB 연결 닫기
    def close(self):
        if self.conn is None:
            return

        if not self.conn.open:
            self.conn = None
            return
        self.conn.close()
        self.conn = None
        
    # DB commit 필요한 쿼리 (INSERT, DELETE)
    def execute(self, sql):
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
        self.conn.commit()
    
    def select_one(self, sql):
        result = None
        
        with self.conn.cursor( ) as cursor:
            cursor.execute(sql)
            result = cursor.fetchone()
        
        return result
    
    def select_all(self, sql):
        result_list = ()
        
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            result_list = cursor.fetchall()
        
        return result_list