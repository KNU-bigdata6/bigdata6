from flask import Flask, render_template, request, jsonify, make_response, Blueprint, redirect, url_for, flash
from flask_login import current_user
from flask_paginate import Pagination, get_page_parameter
from service.board import Board

board = Blueprint('board', __name__, url_prefix='/board')

# 페이지당 아이템 수
PER_PAGE = 10

@board.route('/')
def main():
  if current_user.is_authenticated:
    POSTS = Board.get_post_list()
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

# 게시물 페이지
@board.route('/page/<int:index>')
def post(index):
  if current_user.is_authenticated:
    Board.increase_views(index)
    return render_template("page.html", index=index, login=True)
  else:
      # 경고문 띄우기
      flash("not login")
      return redirect(url_for('main.login'))

# 게시물 등록
@board.route('/page/write', methods=['GET', 'POST'])
def write():
  if current_user.is_authenticated:
    if request.method == 'GET':
      return render_template("write.html", login=True)
    else:
      title = request.form['title']
      contents = request.form['contents']
      city = request.form['city']
      district = request.form['district']
      
      index = Board.register_post(current_user.user_id, title, contents, current_user.name, city, district)      
      return redirect(url_for('board.post', index=index))
  else:
      # 경고문 띄우기
      flash("not login")
      return redirect(url_for('main.login'))
    
#관심 목록
@board.route('/page/interests')
def interests():
  return "내 관심 리스트"