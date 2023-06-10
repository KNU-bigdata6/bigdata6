from flask import Flask, render_template, request, jsonify, make_response, Blueprint, redirect, url_for, flash
from flask_login import current_user
from flask_paginate import Pagination, get_page_parameter
from .user_board import Board

board = Blueprint('board', __name__, url_prefix='/board')

# 페이지당 아이템 수
PER_PAGE = 10

@board.route('/')
def main():
  if current_user.is_authenticated:
    category = request.args.get('category')
    
    # 검색을 안한 경우
    if not category:
      POSTS = sorted(Board.get_post_list(), reverse=True)
    # 검색을 한 경우
    else:
      # 위치 검색
      if category=='location':
        POSTS = sorted(Board.get_by_location(category, request.args.get('city'), request.args.get('district')), reverse=True)
      # 위치 검색이 아닌경우
      else:
        POSTS = sorted(Board.get_by_category_and_query(category, request.args.get('query')), reverse=True)
        
    page = request.args.get(get_page_parameter(), type=int, default=1)
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
    page = Board.get_post_content(index)
    _, _, user_id, title, content, name, city, district, views, date = page
    
    comments = Board.get_post_all_comment(index)
    
    return render_template("page.html", index=index, user_id = user_id, title=title, content = content, name=name, city=city, district = district, views=views, date=date, cur_name = current_user.name, cur_user_id = current_user.user_id, comments = comments, login=True)
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
      content = request.form['content']
      city = request.form['city']
      district = request.form['district']
      
      index = Board.register_post(current_user.user_id, title, content, current_user.name, city, district)      
      return redirect(url_for('board.post', index=index))
  else:
      # 경고문 띄우기
      flash("not login")
      return redirect(url_for('main.login'))

# 게시물 수정
@board.route('/page/edit/<int:index>', methods=['POST'])
def edit(index):
  if current_user.is_authenticated:
    data = Board.get_post_content(index)
    title = data[3]
    content = data[4]
    return render_template("edit.html", index=index, title=title, content=content, login=True)
  else:
      # 경고문 띄우기
      flash("not login")
      return redirect(url_for('main.login'))

#게시글 업데이트
@board.route('/page/update/<int:index>', methods=['POST'])
def update(index):
  if current_user.is_authenticated:
    title = request.form['title']
    content = request.form['content']
    city = request.form['city']
    district = request.form['district']
    Board.update_post(index, title, content, city, district)
    return redirect(url_for('board.post', index=index))
  else:
    # 경고문 띄우기
    flash("not login")
    return redirect(url_for('main.login'))

# 게시물 삭제
@board.route('/page/delete/<int:index>', methods=['POST'])
def delete(index):
  if current_user.is_authenticated:
      Board.delete_post(index)
      return redirect(url_for('board.main'))
  else:
      # 경고문 띄우기
      flash("not login")
      return redirect(url_for('main.login'))

# 댓글 등록
@board.route('/comment/write/<int:index>', methods=['POST'])
def comment_wirte(index):
  if current_user.is_authenticated:
      Board.register_comment(index, current_user.user_id, request.form['text'], current_user.name)
      return redirect(url_for('board.post', index=index))
  else:
      # 경고문 띄우기
      flash("not login")
      return redirect(url_for('main.login'))
  
# 댓글 삭제
@board.route('/comment/delete/<int:index>', methods=['POST'])
def comment_delete(index):
  if current_user.is_authenticated:
      Board.delete_comment(request.form['comment_num'], index)
      return redirect(url_for('board.post', index=index))
  else:
      # 경고문 띄우기
      flash("not login")
      return redirect(url_for('main.login'))