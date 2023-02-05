from flask import Flask, request
import os

app = Flask(__name__)

from routes.routes import *

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
