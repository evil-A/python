from book import Book
from recipe import Recipe
from datetime import date


# ... tests ...

canelones = Recipe('Canelones', 4, 30, ['pasta', 'mierda', 'carne humana', 'agua del grifo'],
        'canelones de mierda y carne humana con agua del grifo', 'starter')

tutorial = Book('Tutoriales culinarios')

#tutorial.add_recipe('canelones')
tutorial.add_recipe(canelones)
print(tutorial.get_recipe_by_name(canelones))
#print(tutorial.get_recipe_by_name('mierda'))
#print(tutorial.get_recipes_by_type('starter'))


#print(str(tutorial))


#to_print = str(canelones)
#print(to_print)

#today = date.today()
#print(today)

