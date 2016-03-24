import bottle
import logging
import threading

_local = threading.local()

logging.basicConfig(level=logging.DEBUG)
_logger = logging.getLogger('module')
_local.logger = logging.getLogger('thread-%d' % threading.current_thread().ident)
_logger.info('Reading module')

class ConnectionPool(object):

    def __init__(self):
        self._logger = logging.getLogger('thread-%d' % threading.current_thread().ident)
        self._logger.info('Creating instance by %s', threading.current_thread().name)

    # Returns a connection id. If there is not a connection available, 
    # this method blocks until one is released.
    def adquire_connection(self):
        self._logger.info('Requesting connection.')
        return 1

    #
    # Releases the connection.
    # 
    def release_connection(self, connection_id):
        self._logger.info('Releasing connection %d', connection_id)
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
    _local.logger.info('Executing request from thread %s', threading.current_thread().name)
    return "I'm working!"

@app.route('/function')
def function_scope():
    _local.logger.info('Executing request from thread %s', threading.current_thread().name)
    pool = ConnectionPool()
    return "OK"

@app.route('/thread')
def thread_scope():
    _local.logger.info('Executing request from thread %s', threading.current_thread().name)
    return "OK"

@app.route('/module')
def module_scope():
    _local.logger.info('Executing request from thread %s', threading.current_thread().name)
    pool = get_pool()
    return "OK"

