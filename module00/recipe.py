cookbook = {
  "sandwich": {
    "ingredients": ["ham", "bread", "cheese", "tomatoes"],
    "meal": "lunch",
    "prep_time": 10
  },
  "cake": {
    "ingredients": ["flour", "sugar", "eggs"],
    "meal": "dessert",
    "prep_time": 60
  },
  "salad": {
    "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
    "meal": "lunch",
    "prep_time": 15
  }
}


def print_recipe(recipename):
    print("recipe for", recipename, ":")
    print("Ingredients list:", cookbook[recipename]["ingredients"])
    print("to be eaten for", cookbook[recipename]["meal"], '.')
    print("takes", cookbook[recipename]["prep_time"], "minutes of cooking.")


def delete_recipe(recipename):
    if recipename in cookbook:
        cookbook.pop(recipename, None)


def addrecipe(recipename, ingredientss, meall, prepp_time):
    T = []
    for ingredient in ingredientss:
        T.append(ingredient)
    new_recipe = {"ingredients": T,
                "meal": meall,
                "prep_time": prepp_time, }
    cookbook[recipename] = new_recipe


addrecipe('tacos', ['poulet', 'frites', 'sauce'], 'lunch', 30)


def print_cookbook():
        for recipename in cookbook:
                print_recipe(recipename)


print("Please select an option by typing the corresponding number:")
print("1: Add a recipe", "2: Delete a recipe ", "3: Print a recipe",
    "4: Print the cookbook", "5: Quit", sep='\n')
option = input()
if option == '1':
    newrecipe = input("enter the new recipe name")
    print("enter the recipe's ingredients")
    a = 'a'
    while a != "":
        T = []
        a = input()
        T.append(a)
    newmeal = input("enter its meal type")
    newpreptime = input("enter its preparation time")
    addrecipe(newrecipe, T, newmeal, newpreptime)
elif option == '2':
    recipename = input("enter the name of the recipe you want to delete"))
    delrecipe(recipename)
elif option == '3':
    recipename=input("enter the name of the recipe you want to print"))
    print_recipe(recipename)
elif option == '4':
    print("your cookbook contains :\n")cookbook={
  "sandwich": {
    "ingredients": ["ham", "bread", "cheese", "tomatoes"],
    "meal": "lunch",
    "prep_time": 10
  },
  "cake": {
    "ingredients": ["flour", "sugar", "eggs"],
    "meal": "dessert",
    "prep_time": 60
  },
  "salad": {
    "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
    "meal": "lunch",
    "prep_time": 15
  }
}


def print_recipe(recipename):
    print("recipe for", recipename, ":")
    print("Ingredients list:", cookbook[recipename]["ingredients"])
    print("to be eaten for", cookbook[recipename]["meal"], '.')
    print("takes", cookbook[recipename]["prep_time"], "minutes of cooking.")


def delete_recipe(recipename):
    if recipename in cookbook:
        cookbook.pop(recipename, None)


def addrecipe(recipename, ingredientss, meall, prepp_time):
    T = []
    for ingredient in ingredientss:
        T.append(ingredient)
    new_recipe = {"ingredients": T,
                "meal": meall,
                "prep_time": prepp_time, }
    cookbook[recipename] = new_recipe


addrecipe('tacos', ['poulet', 'frites', 'sauce'], 'lunch', 30)


def print_cookbook():
        for recipename in cookbook:
                print_recipe(recipename)


print("Please select an option by typing the corresponding number:")
print("1: Add a recipe", "2: Delete a recipe ", "3: Print a recipe",
    "4: Print the cookbook", "5: Quit", sep='\n')
option = input()
if option == '1':
    newrecipe = input("enter the new recipe name")
    print("enter the recipe's ingredients")
    a = 'a'
    while a != "":
        T = []
        a = input()
        T.append(a)
    newmeal = input("enter its meal type")
    newpreptime = input("enter its preparation time")
    addrecipe(newrecipe, T, newmeal, newpreptime)
elif option == '2':
    recipename = input("enter the name of the recipe you want to delete")
    delrecipe(recipename)
elif option == '3':
    recipename=input("enter the name of the recipe you want to print")
    print_recipe(recipename)
elif option == '4':
    print("your cookbook contains :\n")
    print_cookbook()
elif option == '5':
    print("Cookbook closed.")
else: print("This option does not exist, please type the corresponding number. \n", "To exit, enter 5.")

    print_cookbook()
elif option == '5':
    print("Cookbook closed.")
else: print("This option does not exist, please type the corresponding number. \n", "To exit, enter 5.")
