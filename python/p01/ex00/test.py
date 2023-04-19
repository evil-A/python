from book import Book
from recipe import Recipe

# ... tests ...

canelones = Recipe('Canelones', 4, 30, ['pasta', 'mierda', 'carne humana', 'agua del grifo'],
        'canelones de mierda y carne humana con agua del grifo', 'starter')

to_print = str(canelones)
print(to_print)

