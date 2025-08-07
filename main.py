from Addition import calculate
from hello import sayhello
from flask import Flask, jsonify

app = Flask(__name__)
num1 = 10
num2 = 5

calculate(num1, num2)
sayhello()

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, world!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
