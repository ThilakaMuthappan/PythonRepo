from flask import Flask, jsonify, request

app = Flask(__name__)

# Initialize an empty list to store strings
string_list = []

@app.route('/add_string', methods=['POST'])
def add_string():
    data = request.get_json()
    if 'string' in data:
        string_list.append(data['string'])
        return jsonify({"message": "String added to the list"}), 200
    else:
        return jsonify({"error": "Please provide 'string' parameter in the request body"}), 400

@app.route('/get_list', methods=['GET'])
def get_list():
    return jsonify({"string_list": string_list}), 200

if __name__ == '__main__':
    app.run(debug=True)