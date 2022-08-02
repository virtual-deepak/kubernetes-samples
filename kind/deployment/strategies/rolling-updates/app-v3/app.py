import os
import socket
from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World running from v3: ' + socket.gethostname()


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=PORT)
