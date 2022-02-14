from flask import request, jsonify

import data
import services.RecipeService as recipeService

def getNames():
    names = recipeService.getNames()
    return jsonify(names), 200


def addRecipe():
    res = recipeService.addRecipe(request.get_json())
    if res:
        return res, 400
    return '', 201


def modifyRecipe():
    res = recipeService.modifyRecipe(request.get_json())
    if res:
        return res, 404
    return '', 204

def getDetails(recipeName):
    details = recipeService.getDetails(recipeName)
    return jsonify(details), 200