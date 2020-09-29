def read_recipes(file_name='recipes.txt'):
    book = {}
    with open(file_name, 'r', encoding='utf-8') as f:
        end_of_file = True
        while end_of_file:
            recipe_name = f.readline().strip()
            ingredient_count = int(f.readline())
            recipe_list = []
            for _ in range(ingredient_count):
                recipe_line = f.readline().split('|')
                recipe = {
                    'ingredient_name': recipe_line[0].strip(),
                    'quantity': int(recipe_line[1]),
                    'measure': recipe_line[2].strip()
                }
                recipe_list.append(recipe)
            book[recipe_name] = recipe_list
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
                        shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
                    else:
                        shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                                    'quantity': ingredient['quantity'] * person_count}
        return shop_list
    else:
        return 'Wrong person number'


shopping_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(shop_list)
