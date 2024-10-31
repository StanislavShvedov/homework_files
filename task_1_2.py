from pprint import pprint

# Task_1
def make_recipe_name(file) -> dict:
    cook_book = {}
    key =''
    for line in file:
        if line.strip() != '' and ' | ' not in line.strip() and len(line.strip()) > 1:
            cook_book[line.strip()] = []
            key = line.strip()
        elif key in cook_book and '|' in line.strip():
            ingredients_dict = {}
            ingredients_dict['ingredient_name'] = line.strip().split(' | ')[0]
            ingredients_dict['quantity'] = line.strip().split(' | ')[1]
            ingredients_dict['measure'] = line.strip().split(' | ')[2]
            cook_book[key].append(ingredients_dict)
    return cook_book

def make_cook_book() -> dict:
    with open('recipes.txt') as recipes:
        cook_book = make_recipe_name(recipes)
    return cook_book

pprint(make_cook_book())

# Task_2
def get_shop_list_by_dishes(dishes: list, person_count: int) -> dict:
    make_cook_book()
    shop_dict = {}
    for key in dishes:
        for product in make_cook_book()[key]:
            shop_dict[product['ingredient_name']] = []
            ingredient = {}
            ingredient['measure'] = product['measure']
            ingredient['quantity'] = int(product['quantity']) * person_count
            shop_dict[product['ingredient_name']].append(ingredient)
    return shop_dict

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

