from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask API!"

# ✅ This is the missing POST route
@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    message = data.get("message", "")
    return jsonify({"response": f"Received: {message}"})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
