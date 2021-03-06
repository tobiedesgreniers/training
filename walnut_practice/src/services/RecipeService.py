import json
import os

from models.recipe import Recipe, RecipeSchema
import data

schema = RecipeSchema(many=True, context=["NAMES"])

def getNames():
    schema = RecipeSchema(many=True)
    schema.context["names"] = True
    recipes = schema.dump(data.recipes)
    return {'recipeNames' : names}


def getDetails(name):
    for item in data['recipes']:
        if item['name'] == name:
            return {'details' : {'ingredients': item['ingredients'], 'numSteps': len(item['instructions'])}}
    else:
        return {}


def addRecipe(recipe):
    exists = [1 for item in data['recipes'] if item['name'] == recipe['name']]
    if exists:
        return {'error': 'Recipe already exists'}
    else:
        data['recipes'].append(recipe)
        saveData(data)
        return


def modifyRecipe(recipe):
    exists = [index for index, item in enumerate(data['recipes']) if item['name'] == recipe['name']]
    if exists:
        data['recipes'][exists[0]]['name'] = recipe['name']
        data['recipes'][exists[0]]['instructions'] = recipe['instructions']
        data['recipes'][exists[0]]['ingredients'] = recipe['ingredients']
        saveData(data)
        return
    else:
        data['recipes'].append(recipe)
        return {'error': 'Recipe does not exist'}