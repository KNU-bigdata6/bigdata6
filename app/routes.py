from flask import Flask, render_template, request
from app import app
L = []


@app.route('/')
def vars():
    L.clear()
    return render_template('home.html')


@app.route('/test', methods=['GET', 'POST'])
def vars2():
    if request.method == 'POST':
        var = request.form['messege']
        L.append([str(var), 'test'])
        return render_template('test.html', data_list=L)
    else:
        L.clear()
        return render_template('test.html')
