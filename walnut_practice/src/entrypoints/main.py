from flask import Flask, request, jsonify
import json
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import data

app = Flask(__name__)


@app.route('/recipes', methods=['GET', 'POST', 'PUT'])
def recipes():
    if request.method == 'GET':
        names = data.getNames()
        return jsonify(names), 200
    
    elif request.method == 'POST':
        res = data.addRecipe(request.get_json())
        if res:
            return res, 400
        return '', 201

    elif request.method == 'PUT':
        res = data.modifyRecipe(request.get_json())
        if res:
            return res, 404
        return '', 204

@app.route('/recipes/details/<string:recipeName>', methods=['GET'])
def get_details(recipeName):
    details = data.getDetails(recipeName)
    return jsonify(details), 200


if __name__ == '__main__':
    app.run()

""" debug=True """