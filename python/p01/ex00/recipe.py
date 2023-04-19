class Recipe:
    name = ""
    cooking_lvl = 0 # int range 1 - 5
    cooking_time = 0 # int minutes positive
    ingredients = [] # list each a string
    description = "" # can be empty
    recipe_type = "" # starter lunch dessert

    def __init__(self, name: str, cooking_lvl: int, cooking_time: int, ingredients: list,
            description: str, recipe_type: str):
        if not isinstance(name, str):
            print("ERROR: Name not a string")
            exit(1)
        if not isinstance(cooking_lvl, int) or not cooking_lvl in (1, 2, 3, 4, 5):
            print("ERROR: cooking level not an integer 1 - 5")
            exit(1)
        if not isinstance(cooking_time, int) or not (cooking_time > 0):
            print("ERROR: cooking time not a positive integer")
            exit(1)
        if not isinstance(ingredients, list):
            print("ERROR: bad ingredients list")
            exit(1)
        else:
            for ing in ingredients:
                if not(isinstance(ing, str)):
                    print("ERROR: bad ingredient")
                    exit(1)
        if not isinstance(recipe_type, str):
            print("ERROR: bad recipe type")
            exit(1)
        try:
            self.name = str(name)
            self.cooking_lvl = int(cooking_lvl)
            self.cooking_time = int(cooking_time)
            self.ingredients = list(ingredients)
            self.description = description
            self.recipe_type = recipe_type
        except:
            raise TypeError

    def __str__(self):
        res = "\nRecipe:"
        res = res + ' ' + self.name + ":\n" 
        res = res + "- Cooking level: " + str(self.cooking_lvl) + '\n'
        res = res + "- Cooking time: " + str(self.cooking_time) + '\n'
        ing_str = ''
        for i in range(len(self.ingredients)):
            ing_str += self.ingredients[i]
            if i != (len(self.ingredients) - 1):
                ing_str += ', '
        res = res + "- List of ingredients: " + ing_str + '\n'
        res = res + "- Descrition: " + self.description + '\n'
        res = res + "- Type of recipe: " + self.recipe_type + '\n'
        return(res)
"""
    def __init__(self, name: str, cooking_lvl: int, cooking_time: int, ingredients: list,
            description: str, recipe_type: str):
        if not (isinstance(name, str) and isinstance(cooking_lvl, int) and cooking_lvl in (1, 2, 3, 4, 5)
                and isinstance(cooking_time, int) and cooking_time > 0 and isinstance(ingredients, list)
                and isinstance(recipe_type, str)):
            print("ERROR: bad declaration")
            exit (1)
        elif not (recipe_type in ('starter', 'lunch', 'dessert')):
            raise ValueError
        else:    
            for ing in ingredients:
                if not(isinstance(ing, str)):
                    raise ValueError
            try:
                self.name = str(name)
                self.cooking_lvl = int(cooking_lvl)
                self.cooking_time = int(cooking_time)
                self.ingredients = list(ingredients)
                self.description = description
                self.recipe_type = recipe_type
            except:
                raise NameError('Assignation error')

"""
