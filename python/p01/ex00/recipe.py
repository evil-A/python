class Recipe:
    def __init__(self, name: str, cooking_lvl: int, cooking_time: int, ingredients: list,
            description: str, recipe_type: str):
        if not isinstance(name, str):
            print("ERROR: Name not a string")
            return None
        if not isinstance(cooking_lvl, int) or not cooking_lvl in (1, 2, 3, 4, 5):
            print("ERROR: cooking level not an integer 1 - 5")
            return None
        if not isinstance(cooking_time, int) or not (cooking_time > 0):
            print("ERROR: cooking time not a positive integer")
            return None
        if not isinstance(ingredients, list):
            print("ERROR: bad ingredients list")
            return None
        else:
            for ing in ingredients:
                if not(isinstance(ing, str)):
                    print("ERROR: bad ingredient")
                    return None
        if not isinstance(recipe_type, str) or not recipe_type in ('starter', 'lunch', 'dessert'):
            print("ERROR: bad recipe type")
            return None
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
