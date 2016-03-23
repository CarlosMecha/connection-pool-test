import bottle

class ConnectionPool(object):

    def __init__(self):
        print "Creating instance"

    # Returns a connection id. If there is not a connection available, 
    # this method blocks until one is released.
    def adquire_connection(self):
        return 1

    #
    # Releases the connection.
    # 
    def release_connection(self, connection_id):
        return True

@bottle.route('/')
def index():
    return "I'm working!"


