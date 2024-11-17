from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample API endpoint
@app.route('/api/message', methods=['GET'])
def get_message():
    return jsonify({"message": "Hello from the backend!"})

# API endpoint to receive data from frontend
@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.json
    return jsonify({"status": "success", "received": data}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
