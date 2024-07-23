import multiprocessing
wsgi_app = "fphlcore.wsgi:application"
workers = multiprocessing.cpu_count() * 2 + 1
bind = "0.0.0.0:8000"
accesslog = "/app/fphlcore/logs/access.log"
errorlog = "/app/fphlcore/logs/error.log"
capture_output = True
pidfile = "/app/fphlcore/logs/prod.pid"
daemon = False
