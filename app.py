
import bottle
import index

app = application = index.app

if __name__ == '__main__':
    bottle.run(app, port=8080)

