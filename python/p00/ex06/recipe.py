recipe1 = {
        "ingredients" : ["ham", "bread", "cheese", "tomatoes"],
        "meal" : "lunch",
        "prep_time" : 10
        }

recipe2 = {
        "ingredients" : ["flour", "sugar", "eggs"],
        "meal" : "dessert",
        "prep_time" : 60
        }

recipe3 = {
        "ingredients" : ["avocado", "arugula", "tomatoes", "spinach"],
        "meal" : "lunch",
        "prep_time" : 15
        }

cookbook = {
        "Sandwich" : recipe1,
        "Cake" : recipe2,
        "Salad" : recipe3
        }

loop = True
num = int(4)

def allNames():
    print(*cookbook, "\n")

def delRecipe():
    print("Please enter a recipe name to delete:")
    erase = input()
    cookbook.pop(erase, -1)

def printRecipe():
    print("Please enter a recipe name to get its details:")
    show = input()
    try:
        cookbook[show]
        print("Recipe for", show)
        print("Ingredients list:", cookbook[show]['ingredients'])
        print("To be eaten for", cookbook[show]['meal'] + '.')
        print("Takes", cookbook[show]['prep_time'], "minutes of cooking.\n")
    except:
        print("Doesn't exists\n")

def addRecipe():
    global num
    try:
        print("Enter a name:")
        recipename = 'recipe' + str(num)
        name = input()
        cookbook[name] = {}
        cookbook[name] = recipename
        ingLst = []
        ing = "empty"
        print("Enter ingredients:")
        while (ing != ''):
            ing = ""
            ing = input()
            ingLst.append(ing)
        ingLst.remove('')
        cookbook[name] = {
                "ingredients": ingLst,
                "meal": input("Enter a meal type:\n"),
                "prep_time": int(input("Enter a preparation time:\n"))
                }
        num += 1
    except:
        print("Not valid recipe")
        cookbook.pop(name)
        return

def quit():
    global loop
    loop = False


def options():
    print("List of available options:\n"
        "1: Add a recipe\n"
        "2: Delete a recipe\n"
        "3: Print a recipe\n"
        "4: Print the cookbook\n"
        "5: Quit\n")
    print("Please select an option: \n")

if __name__ == "__main__":
   
    print("Welcome to the Python Cookbook !")

    while (loop):
        options()
        menu = input()
        print("\n")
        if menu == "1":
            addRecipe()
        elif menu == "2":
            delRecipe()
        elif menu == "3":
            printRecipe()
        elif menu == "4":
            allNames()
        elif menu == "5":
            quit()
        else:
            pass

