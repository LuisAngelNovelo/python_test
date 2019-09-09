# Laucher
from gevent.pywsgi import WSGIServer
from config import app

http_server = WSGIServer(("", 9000), app)
http_server.serve_forever()
