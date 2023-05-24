from db_model.db_connection import USER_DB, conn_db
from db_model.board_query import BoardQuery
from datetime import datetime
from service.user import User

class Board():
    @staticmethod
    def get_post_list():
        conn_db(USER_DB)

        sql = BoardQuery.find_all()
        result = USER_DB.select_all(sql)
      
        return result
      
    @staticmethod
    def register_post(user_id, title, content, name, city, district):
        conn_db(USER_DB)
                
        # 회원 번호 조회
        user = User.find_member(user_id)
        id = user.id
        
        sql = BoardQuery.save(id, user_id, title, content, name, city, district, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        index = USER_DB.execute_and_return_index(sql)
        return index
    
    @staticmethod
    def increase_views(index):
        conn_db(USER_DB)
        
        sql = BoardQuery.increase_one(index)
        USER_DB.execute(sql)
