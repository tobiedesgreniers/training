from marshmallow import Schema, fields

class Recipe():
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
    

    def __repr__(self):
        return f'Recipe({self.name})'


class RecipeSchema(Schema):
    name = fields.Dict(fields.Str())
    ingredients = fields.Dict(fields.List(fields.Str()))
    instructions = fields.Dict(fields.List(fields.Str()))