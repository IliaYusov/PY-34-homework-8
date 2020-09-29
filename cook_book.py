def read_recipes(file_name='recipes.txt'):
    book = {}
    with open(file_name) as f:
        end_of_file = True
        while end_of_file:
            recipe_name = f.readline().strip()
            ingredient_count = int(f.readline())
            recipe = {}
            recipe_list = []
            for _ in range(ingredient_count):
                print(recipe_list)
                recipe['ingredient_name'], recipe['quantity'], recipe['measure'] = f.readline().strip().split('|')
                recipe_list.append(recipe)
            book[recipe_name] = recipe_list[:]
            end_of_file = f.readline()
    return book

def get_shop_list_by_dishes(dishes, person_count):
    if person_count > 0:
        shop_list = {}
        cook_book = read_recipes()
        for recipe in cook_book:
            if recipe in dishes:
                for ingredient in cook_book[recipe]:
                    if ingredient['ingredient_name'] in shop_list:
                        shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['measure'] * person_count
                    else:
                        shop_list[ingredient['ingredient_name']] = {'meausure': ingredient['measure'], 'quantity': ingredient['measure'] * person_count}       
    else:
        return 'Wrong person number'
        

cook_book = read_recipes()
##shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
##print(cook_book.items())
##print(shop_list)
