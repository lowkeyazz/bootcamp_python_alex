import sys


class Recipe:
    def __init__(self, recipe_name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        if recipe_name == '' or type(recipe_name) != str:
            sys.exit("ERROR")
        self.recipe_name = recipe_name
        if cooking_lvl in [1, 2, 3, 4, 5]:
            self.cooking_lvl = cooking_lvl
        else:
            sys.exit("ERROR")
        if type(cooking_time) != int or cooking_time <= 0:
            sys.exit("ERROR")
        self.cooking_time = cooking_time
        for a in ingredients:
            if type(a) != str:
                sys.exit("ERROR")
        if type(ingredients) != list:
            sys.exit("ERROR")
        self.ingredients = ingredients
        if type(description) != str:
            sys.exit("ERROR")
        self.description = description
        if not recipe_type in ["starter", "lunch", "dessert"]:
            sys.exit("ERROR")
        self.recipe_type = recipe_type

    def __str__(self):
        return 'The Recipe ' + str(self.recipe_name) + ' is level ' + str(self.cooking_lvl) + ',it takes ' + str(self.cooking_time) + ' mins to cook, it contains ' + str(self.ingredients) + ' ,its description is ' + str(self.description)+' ,and it is taken as a ' + str(self.recipe_type)+''
