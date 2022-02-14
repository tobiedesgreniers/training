from flask import Blueprint

import controllers.RecipeController as recipeController

recipe_bp = Blueprint('recipe_bp', __name__)

recipe_bp.route('/recipes', methods=['GET']) (recipeController.getNames)
recipe_bp.route('/recipes', methods=['POST']) (recipeController.addRecipe)
recipe_bp.route('/recipes', methods=['PUT']) (recipeController.modifyRecipe)
recipe_bp.route('/recipes/details/<string:recipeName>', methods=['GET']) (recipeController.getDetails)
