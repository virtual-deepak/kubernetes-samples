import os
import requests
from flask import Flask


app = Flask(__name__)


@app.route('/')
def get_external_data():
    result = requests.get(url='http://external-service:9000')
    return 'Response from external service: ' + str(result.text)


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 80))
    app.run(debug=True, host='0.0.0.0', port=PORT)
