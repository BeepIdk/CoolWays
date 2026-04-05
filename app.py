from flask import Flask, request, jsonify

app = Flask(__name__)

data_store = {"target": "", "code": ""}

@app.route('/', methods=['GET'])
def get_code():
    global data_store
    response = jsonify(data_store)
    data_store = {"target": "", "code": ""}
    return response

@app.route('/set', methods=['POST'])
def set_code():
    global data_store
    new_data = request.json
    data_store["target"] = new_data.get("target", "")
    data_store["code"] = new_data.get("code", "")
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)