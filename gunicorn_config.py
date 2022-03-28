bind = '0.0.0.0:5000'
loglevel = 'debug'
accesslog = 'logs_gunicorn/access_log_yourapp'
acceslogformat ="%(h)s %(l)s %(u)s %(t)s %(r)s %(s)s %(b)s %(f)s %(a)s"
errorlog =  'errors_gunicorn/error_log_yourapp'
