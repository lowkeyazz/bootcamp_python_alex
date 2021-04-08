from recipe import Recipe
import datetime
import sys


class Book:
    def __init__(self, name, last_update, creation_date, recipe_list):
        if name == '' or type(name) != str:
            sys.exit("ERROR \n Type 'str' required ")
        self.name = name
        self.last_update = last_update
        self.creation_date = creation_date
        if type(recipe_list) != dict or (len(recipe_list) != 3 or ("starter" not in recipe_list) or ("lunch" not in recipe_list) or ("dessert" not in recipe_list)):
            sys.exit("ERROR \n Type 'dict' required isn't adaptable")
        self.recipe_list = recipe_list

    def get_recipe_by_name(self, name):
        starter = list(self.recipe_list["starter"])
        lunch = list(self.recipe_list["lunch"])
        dessert = list(self.recipe_list["dessert"])
        a = 0
        b = 0
        c = 0
        for i in starter:
            if i in lunch:
                a = 1
        for i in starter:
            if i in dessert:
                b = 1
        for i in lunch:
            if i in dessert:
                c = 1
        if (a == 1) or (b == 1) or (c == 1):
            return "You have some meals that are the same"
        if name in starter:
            return self.recipe_list["starter"][name]
        elif name in lunch:
            return self.recipe_list["lunch"][name]
        elif name in dessert:
            return self.recipe_list["dessert"][name]
        else:
            return "This name dosen't occure on the recipe list"

    def get_recipes_by_types(self, recipe_type):
        if recipe_type == "starter":
            return list(self.recipe_list["starter"])
        elif recipe_type == "lunch":
            return list(self.recipe_list["lunch"])
        elif recipe_type == "dessert":
            return list(self.recipe_list["dessert"])
        else:
            return "There is no recipe with that type."

    def add_recipe(self, recipe):
        if type(recipe) != Recipe:
            print("Please create the recipe first then add it to the book.")
            return
        self.recipe_list[recipe.recipe_type][recipe.recipe_name] = recipe
        self.last_update = datetime.datetime.now()
        return
