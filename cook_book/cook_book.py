import json
from pprint import pprint
from netology.decorators import loger

path_to_log = r'C:\Users\user\Documents\Python\netology\decorators\cook_book'


def cookbook():
    cook_book = {}
    a = []
    with open('recipes.txt', 'r', encoding='utf-8') as f:
        for dish in f:
            for ingredient in range(int(f.readline()) + 1):
                norm_str = f.readline().strip().split(' | ')
                if len(norm_str) == 3:
                    items = {'ingredient_name': norm_str[0], 'quantity': norm_str[1], 'measure': norm_str[2]}
                    a.append(items)
            cook_book[dish.strip()] = a
            a = []
        return cook_book


@loger.log_deco(path_to_log)
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ing in cookbook()[dish]:
            shop_list.update({ing['ingredient_name']: {'measure': ing['measure'],
                                                       'quantity': int(ing['quantity']
                                                                       ) * person_count * dishes.count(dish)}})
    return shop_list


cook_json = json.dumps(cookbook(), ensure_ascii=False, indent=4)
print(cook_json)
print()
pprint(get_shop_list_by_dishes(['Омлет', 'Утка по-пекински', 'Омлет'], 2))

