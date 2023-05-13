#from flask import session
#from flask_socketio import emit, join_room, leave_room, Namespace
#from flask_login import login_user, logout_user, current_user
#from service.user import User

#class ChatNamepsace(Namespace):

#    def on_connect(self):
#        pass

#    def on_disconnect(self):
#        pass

#    def on_joined(self, data):
#        room = session.get('room')
#        join_room(room)
#        emit('status', {'msg': current_user.get_user_id() + '님이 입장하셨습니다'}, room=room)

    #socket.on('status', function(data) {} 클라이언트가 받는 형태

#    def on_text(self, data):
#        print("성공")
#        room = session.get('room')
#        emit('message', {'msg': current_user.get_user_id() + ':' + data['msg']}, room=room)
    #클라이언트가 socket.emit('text', 'Hello, server!'); 하면 on_(text) 가 실행

#    def on_left(self, data):
#        room = session.get('room')
#        leave_room(room)
#        emit('status', {'msg': current_user.get_user_id() + '님이 퇴장하셨습니다'}, room=room)

