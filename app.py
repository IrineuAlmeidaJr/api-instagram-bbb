from flask import Flask, request, abort

app = Flask(__name__)

from routes.routes import *

if __name__ == '__main__':
    app.run(3000)
