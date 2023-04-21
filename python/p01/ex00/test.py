from book import Book
from recipe import Recipe
from datetime import date


# ... tests ...

print("Define recipe: Canelones\n")
canelones = Recipe('Canelones', 4, 30, ['pasta', 'mierda', 'carne humana', 'agua del grifo'],
        'canelones de mierda y carne humana con agua del grifo', 'starter')

print("Define recipe: Canelones2\n")
canelones2 = Recipe('Canelones2', 4, 30, ['pasta', 'mierda', 'carne humana', 'agua del grifo'],
        'canelones de mierda y carne humana con agua del grifo', 'starter')

print("Define book: Tutoriales culinarios\n")
tutorial = Book('Tutoriales culinarios')

print("Adding Canelones to Tutoriales\n")
tutorial.add_recipe(canelones)
print("Adding Canelones2 to Tutoriales\n")
tutorial.add_recipe(canelones2)
print("Get Canelones from Tutoriales")
print(tutorial.get_recipe_by_name('Canelones'))
print("Get Canelones2 from Tutoriales")
print(tutorial.get_recipe_by_name('Canelones2'))
print("Get Canelones3 from Tutoriales\n")
print(tutorial.get_recipe_by_name('Canelones3'))
print("Get recipes of type starter\n")
print(tutorial.get_recipes_by_types('starter'))
print("Get recipes of type dessert")
print(tutorial.get_recipes_by_types('dessert'))

print("Define wrong recipes\n")

canelones3 = Recipe(3, 4, 30, ['pasta', 'mierda', 'carne humana', 'agua del grifo'],
        'canelones de mierda y carne humana con agua del grifo', 'starter')
canelones4 = Recipe('Canelones3', 0, 30, ['pasta', 'mierda', 'carne humana', 'agua del grifo'],
        'canelones de mierda y carne humana con agua del grifo', 'starter')
canelones5 = Recipe('Canelones3', 4, -30, ['pasta', 'mierda', 'carne humana', 'agua del grifo'],
        'canelones de mierda y carne humana con agua del grifo', 'starter')
canelones6 = Recipe('Canelones3', 4, 30, 'pasta',
        'canelones de mierda y carne humana con agua del grifo', 'starter')
canelones7 = Recipe('Canelones3', 4, 30, [42, 'mierda', 'carne humana', 'agua del grifo'],
        'canelones de mierda y carne humana con agua del grifo', 'starter')
canelones8 = Recipe('Canelones3', 4, 30, ['pasta', 'mierda', 'carne humana', 'agua del grifo'],
        'canelones de mierda y carne humana con agua del grifo', 'dinner')

