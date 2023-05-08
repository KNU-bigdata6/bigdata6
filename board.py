from flask import Flask, render_template, request, jsonify, make_response, Blueprint, redirect, url_for, flash
from flask_login import current_user
from flask_paginate import Pagination, get_page_parameter

board = Blueprint('board', __name__, url_prefix='/board')

# 게시물 데이터(임시 - db 수정 헤야함)
POSTS = [
  {'index' : 1, 'title' : '제목 1', 'nickname' : '닉네임 1', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 2', 'nickname' : '닉네임 2', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 3', 'nickname' : '닉네임 3', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 4', 'nickname' : '닉네임 4', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 5', 'nickname' : '닉네임 5', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 6', 'nickname' : '닉네임 6', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 7', 'nickname' : '닉네임 7', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 8', 'nickname' : '닉네임 8', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 9', 'nickname' : '닉네임 9', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 10', 'nickname' : '닉네임 10', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 11', 'nickname' : '닉네임 11', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 12', 'nickname' : '닉네임 12', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 13', 'nickname' : '닉네임 13', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 14', 'nickname' : '닉네임 14', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 15', 'nickname' : '닉네임 15', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 16', 'nickname' : '닉네임 16', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 17', 'nickname' : '닉네임 17', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 18', 'nickname' : '닉네임 18', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 19', 'nickname' : '닉네임 19', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 20', 'nickname' : '닉네임 20', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 1', 'nickname' : '닉네임 1', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 2', 'nickname' : '닉네임 2', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 3', 'nickname' : '닉네임 3', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 4', 'nickname' : '닉네임 4', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 5', 'nickname' : '닉네임 5', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 6', 'nickname' : '닉네임 6', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 7', 'nickname' : '닉네임 7', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 8', 'nickname' : '닉네임 8', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 9', 'nickname' : '닉네임 9', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 10', 'nickname' : '닉네임 10', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 11', 'nickname' : '닉네임 11', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 12', 'nickname' : '닉네임 12', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 13', 'nickname' : '닉네임 13', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 14', 'nickname' : '닉네임 14', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 15', 'nickname' : '닉네임 15', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 16', 'nickname' : '닉네임 16', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 17', 'nickname' : '닉네임 17', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 18', 'nickname' : '닉네임 18', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 19', 'nickname' : '닉네임 19', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 20', 'nickname' : '닉네임 20', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 1', 'nickname' : '닉네임 1', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 2', 'nickname' : '닉네임 2', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 3', 'nickname' : '닉네임 3', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 4', 'nickname' : '닉네임 4', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 5', 'nickname' : '닉네임 5', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 6', 'nickname' : '닉네임 6', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 7', 'nickname' : '닉네임 7', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 8', 'nickname' : '닉네임 8', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 9', 'nickname' : '닉네임 9', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 10', 'nickname' : '닉네임 10', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 11', 'nickname' : '닉네임 11', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 12', 'nickname' : '닉네임 12', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 13', 'nickname' : '닉네임 13', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 14', 'nickname' : '닉네임 14', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 15', 'nickname' : '닉네임 15', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 16', 'nickname' : '닉네임 16', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 17', 'nickname' : '닉네임 17', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 18', 'nickname' : '닉네임 18', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 19', 'nickname' : '닉네임 19', 'date' : '2023-01-01'},
  {'index' : 1, 'title' : '제목 20', 'nickname' : '닉네임 20', 'date' : '2023-01-01'}
]

# 페이지당 아이템 수
PER_PAGE = 10

@board.route('/')
def main():
  if current_user.is_authenticated:
    # 현재 페이지 가져오기
    page = request.args.get(get_page_parameter(), type=int, default=1)
    
    # 페이징을 위해 변수 생성
    start_idx = (page-1) * PER_PAGE
    end_idx = start_idx + PER_PAGE
    current_post = POSTS[start_idx:end_idx]
    
    pagination = Pagination(page=page, total=len(POSTS), per_page=PER_PAGE, css_framework='bootstrap4')
    
    return render_template("board.html", posts=current_post, pagination=pagination, login=True)
  else:
    # 경고문 띄우기
      flash("not login")
      return redirect(url_for('main.login'))

# 게시물
@board.route('/page/<int:index>')
def post(index):
  if current_user.is_authenticated:
    return render_template("page.html", index=index, login=True)
  else:
      # 경고문 띄우기
      flash("not login")
      return redirect(url_for('main.login'))

# 게시물 등록
@board.route('/page/write')
def write():
  if current_user.is_authenticated:
    return render_template("write.html", login=True)
  else:
      # 경고문 띄우기
      flash("not login")
      return redirect(url_for('main.login'))