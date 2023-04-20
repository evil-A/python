import time
from recipe import Recipe
from datetime import date

class Book:
    name = "" #name of the book
    last_update = () #date of the las update
    creation_date = () #creation date datetime???
    recipes_list = [] # dctionary 3 keys: "starter", "lunch", "dessert"

    def __init__(self, name: str):
        if not isinstance(name, str):
            print("ERROR: name is not a string")
            exit(1)
        else:
            self.name = str(name)
            self.last_update = date.today()
            self.creation_date = date.today()
            self.recipes_list = {'starter': [], 'lunch': [], 'dessert': []}

    def __str__(self):
        res = "\nBook:"
        res = res + ' ' + self.name + ":\n"
        res = res + "- Last update: " + str(self.last_update) + '\n'
        res = res + "- Creation date: " + str(self.creation_date) + '\n'
        reci_str = ''
        for i in range(len(self.recipes_list)):
            reci_str += self.recipes_list[i]
            if i != (len(self.recipes_list) - 1):
                reci_str += ', '
        res = res + "- List of recipes: " + reci_str + '\n'
        return(res)


    def get_recipe_by_name(self, name):
        # bucle que recorra el dicionario por clave y bucle que recorra las listas
        if name in self.recipes_list:
            return(name)
        return(name, " not in " + self.name)
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        #... Your code here ...

    def add_recipe(self, recipe):
        if not isinstance(recipe, Recipe):
            print("ERROR: not a recipe")
            return None
        self.recipes_list[recipe.recipe_type] = recipe
        self.last_update = date.today()
        """Add a recipe to the book and update last_update"""
        #... Your code here ...
'''
    def get_recipes_by_type(self, recipe_type):
        rev_dict = {}
        for key, recipe_type in self.recipes_list.recipe_type():
            rev_dict.setdefault(value, set()).add(key)
        result = [key for key, values in rev_dict.items()
                              if len(values) > 1]
        print("list of recipes", str(result))
        """Get all recipe names for a given recipe_type """
        #... Your code here ...
'''

