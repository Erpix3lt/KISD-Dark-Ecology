from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()  # Get JSON data from request
    a = data.get('a')  # Extract 'a' from JSON
    b = data.get('b')  # Extract 'b' from JSON
    result = a + b  # Calculate the sum
    return jsonify({'result': result})  # Return result as JSON

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500)  # Run server on all available IPs
