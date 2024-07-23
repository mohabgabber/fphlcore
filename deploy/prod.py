import multiprocessing
wsgi_app = "fphlcore.wsgi:application"
workers = multiprocessing.cpu_count() * 2 + 1
bind = "0.0.0.0:8000"
capture_output = True
daemon = False
