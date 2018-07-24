from eve import Eve

from eventcapture.auth import Auth


app = Eve(auth=Auth)

if __name__ == '__main__':
    app.run()
