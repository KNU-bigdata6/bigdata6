
bind = '0.0.0.0:8000'
workers = 2
errorlog = './gunicorn_log/errorlog.txt'
accesslog = './gunicorn_log/accesslog.txt'
timeout = 120