from flask import Flask, jsonify
from models import pizza
from flask import abort
from flask import make_response
from flask import request

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

@app.route("/api/v1/pizza/", methods=["GET"])
def pizza_list_api_v1():
    return jsonify(pizza.all())

@app.route("/api/v1/pizza/<int:pizza_id>", methods=["GET"])
def get_pizza(topping_id):
    topping = pizza.get(topping_id)
    if not topping:
        abort(404)
    return jsonify({"topping": topping})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)

@app.route("/api/v1/pizza/", methods=["POST"])
def create_pizza():
    if not request.json or not 'title' in request.json:
        abort(400)
    topping = {
        'id': pizza.all()[-1]['id'] + 1,
        'topping1': request.json['topping1'],
        'topping2': request.json.get('topping2', ""),
        'done': False
    }
    pizza.create(topping)
    return jsonify({'topping': topping}), 201

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)

@app.route("/api/v1/pizza/<int:topping_id>", methods=['DELETE'])
def delete_pizza(topping_id):
    result = pizza.delete(topping_id)
    if not result:
        abort(404)
    return jsonify({'result': result})

@app.route("/api/v1/pi/<int:topping_id>", methods=["PUT"])
def update_pizza(topping_id):
    topping = pizza.get(topping_id)
    if not topping:
        abort(404)
    if not request.json:
        abort(400)
    data = request.json
    if any([
        'topping1' in data and not isinstance(data.get('topping1'), str),
        'topping2' in data and not isinstance(data.get('topping2'), str),
        'done' in data and not isinstance(data.get('done'), bool)
    ]):
        abort(400)
    pizza = {
        'topping1': data.get('topping1', topping['topping1']),
        'topping2': data.get('topping2', topping['topping2']),
        'done': data.get('done', topping['done'])
    }
    pizza.update(topping_id, topping)
    return jsonify({'topping': topping})

if __name__ == "__main__":
    app.run(debug=True)