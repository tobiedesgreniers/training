from marshmallow import EXCLUDE, Schema, fields, post_load, pre_dump

class Recipe():
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
    

    def __repr__(self):
        return f'Recipe({self.name})'

    def get_name(self):
        return self.name


class RecipeSchema(Schema):
    
    ingredients = fields.List(fields.Str())
    instructions = fields.List(fields.Str())
    name = fields.Str()

    @pre_dump(pass_many=True)
    def wrap(self, data, context):
        if context.get("names"):
            data.get('name')
        self.name_list.append(data.get("name"))
