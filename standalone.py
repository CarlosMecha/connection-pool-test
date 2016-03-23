
import bottle
import index


def main():
    bottle.run(index.app, port=8080)

if __name__ == '__main__':
    main()

