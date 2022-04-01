from flask import Flask, jsonify
from datetime import datetime
app = Flask(__name__)

app.route('/')
def index():
    return jsonify({'message': f'Hello World! current date time is {datetime.now()}'})
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    