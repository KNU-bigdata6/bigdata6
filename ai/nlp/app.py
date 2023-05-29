from . import app


if __name__ == '__main__':
    #    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 5000)), app)
    app.run(host='0.0.0.0',port=8002)
