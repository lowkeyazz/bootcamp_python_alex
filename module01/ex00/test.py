import sys
from book import Book
from recipe import Recipe
import datetime

tea = Recipe("tea", 1, 10, ["water", "teaseeds", "mint","sugar"], " a traditional moroccan drink", "starter")
kouskous = Recipe("kouskous", 4, 60, ["semolina", "carrots", "chicken", "tomatoes"], " a traditional moroccan dish", "lunch")
chbakia = Recipe("chbakia", 2, 20, ["flour", "honey", "sesame"], " a traditional moroccan dessert", "dessert")

recipees = {"starter": {tea.recipe_name: tea},
            "lunch": {kouskous.recipe_name: kouskous},
            "dessert": {chbakia.recipe_name: chbakia}
            }
magazine = Book("magazine", datetime.datetime.now(),datetime.datetime.now(), recipees)

print(tea)

print(magazine.get_recipes_by_types("dessert"))

print(magazine.get_recipe_by_name("kouskous"))

msemen = Recipe("msemen", 3, 30, ["flour", "oil", "butter"], " a traditional moroccan bread ", "starter")


magazine.add_recipe(msemen)

print(magazine.get_recipes_by_types("starter"))
