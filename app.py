from flask import Flask, jsonify, request

app = Flask('Flask tutorial')

# Regresar un string
@app.route('/', methods=['GET'])
def home():
    return 'hello world'


# regresar un json
@app.route('/json-friend', methods=['GET'])
def return_a_json():
    hi = {
        "id": "meep",
        "message": "hello world"
    }

    return jsonify(hi)


# leer el body que se pasa desde el request
@app.route('/add-numbers', methods=['POST'])
def do_something_with_body():
    content = request.json

    result = content[0] + content[1]

    return jsonify(result)


# correr con debug para que se recargue solito cuando haya cambios
app.run(debug=True)
