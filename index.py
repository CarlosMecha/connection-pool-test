import bottle
import threading

class ConnectionPool(object):

    def __init__(self):
        print "Creating instance by ", threading.current_thread().name

    # Returns a connection id. If there is not a connection available, 
    # this method blocks until one is released.
    def adquire_connection(self):
        return 1

    #
    # Releases the connection.
    # 
    def release_connection(self, connection_id):
        return True

_pool = None

def get_pool():

    global _pool

    if _pool is None:
        _pool = ConnectionPool()
    return _pool

app = bottle.Bottle()

@app.route('/')
def index():
    print "Executing request from thread ", threading.current_thread().name
    return "I'm working!"

@app.route('/function')
def function_scope():
    print "Executing request from thread ", threading.current_thread().name
    pool = ConnectionPool()
    return "OK"

@app.route('/thread')
def thread_scope():
    print "Executing request from thread ", threading.current_thread().name
    return "OK"

@app.route('/module')
def module_scope():
    print "Executing request from thread ", threading.current_thread().name
    pool = get_pool()
    return "OK"

