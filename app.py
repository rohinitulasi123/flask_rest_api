from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage
users = {}

# Home route
@app.route('/')
def home():
    return "Welcome to the Flask API! <br><br> API development fundamentals."

# GET: Return all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# POST: Add a new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user_id = data.get("id")
    name = data.get("name")
    
    if user_id in users:
        return jsonify({"message": "User already exists"}), 400
    
    users[user_id] = {"name": name}
    return jsonify({"message": "User added successfully"}), 201

# PUT: Update an existing user
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"message": "User not found"}), 404
    
    data = request.get_json()
    users[user_id]["name"] = data.get("name")
    return jsonify({"message": "User updated successfully"})

# DELETE: Delete a user
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"message": "User not found"}), 404

    del users[user_id]
    return jsonify({"message": "User deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
