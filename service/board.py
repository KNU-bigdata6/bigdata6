from db_model.db_connection import USER_DB, conn_db
from db_model.board_query import BoardQuery
from datetime import datetime
from service.user import User

class Board():
    # 게시판 게시글 전체 조회
    @staticmethod
    def get_post_list():
        conn_db(USER_DB)

        sql = BoardQuery.find_all()
        result = USER_DB.select_all(sql)
      
        return result
    
    # 게시글 내용 조회
    @staticmethod
    def get_post_content(index):
        conn_db(USER_DB)
        
        sql = BoardQuery.find_by_index(index=index)
        result = USER_DB.select_one(sql)
        
        return result
    
    # 게시글 검색
    def get_by_category_and_query(category, query):
        conn_db(USER_DB)
        
        print(category, query)
        if category == 'title':
            sql = BoardQuery.find_all_by_title(query)

        elif category == 'name':
            sql = BoardQuery.find_all_by_name(query)
        
        elif category == 'user_id':
            sql = BoardQuery.find_all_by_userid(query)
        
        print(sql)
        result = USER_DB.select_all(sql)
        
        return result

    # 게시글 등록
    @staticmethod
    def register_post(user_id, title, content, name, city, district):
        conn_db(USER_DB)
                
        # 회원 번호 조회
        user = User.find_member(user_id)
        id = user.id
        
        sql = BoardQuery.save(id, user_id, title, content, name, city, district, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        index = USER_DB.execute_and_return_index(sql)
        return index

    # 게시글 삭제
    @staticmethod
    def delete_post(index):
        conn_db(USER_DB)

        sql = BoardQuery.delete_by_index(index)
        USER_DB.execute(sql)
        
        SUCCESS = True
        return SUCCESS
    
    # 게시글 수정
    @staticmethod
    def update_post(index, title, content, city, district):
        conn_db(USER_DB)

        sql = BoardQuery.full_post_update(index, title, content, city, district, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        USER_DB.execute(sql)
        
        SUCCESS = True
        return SUCCESS
    
    # 조회수 증가
    @staticmethod
    def increase_views(index):
        conn_db(USER_DB)
        
        sql = BoardQuery.increase_one(index)
        USER_DB.execute(sql)
        

