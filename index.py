import bottle
import logging
import redis
import threading

logging.basicConfig(level=logging.DEBUG)

_logger = logging.getLogger('module')
_logger.info('Reading module')

_redis_pool = redis.BlockingConnectionPool(host='localhost', port=6379, db=9)
_redis_client = None

EXPIRATION = 60 * 5 # 5 minutes

def get_redis_connection():
    global _redis_client
    if _redis_client is None:
        _logger.info('Creating Redis client from thread %s', threading.current_thread().name)
        _redis_client = redis.Redis(connection_pool=_redis_pool)
    return _redis_client

app = bottle.Bottle()

@app.route('/')
def index():
    log('GET', '')
    return 'I\'m doing great!'

@app.get('/<key>')
def get_key(key):
    log('GET', key)
    res = get_redis_connection().get(key)
    return res if res else 'Key %s not found' % key

@app.post('/<key>')
def set_key(key):
    log('POST', key)
    content = bottle.request.body.getvalue()
    res = get_redis_connection().setex(key, content, EXPIRATION)
    return 'Key %s stored' % key if res else 'Key %s not stored' % key

def log(method, key):
    name = threading.current_thread().name
    logger = logging.getLogger('thread-%s' % name)
    logger.info('Executing %s /%s from thread %s', method, key, name)

