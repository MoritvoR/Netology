def get_shop_list_by_dishes(dishes: list, person_count: int):
    """Counts the number of products"""
    cook_book = {}
    with open('in_put.txt', 'r', encoding='utf-8') as in_put:
        for line in in_put:
            food_name = line.strip()
            counter = int(in_put.readline())
            structure_list = []
            for now in range(counter):
                ingredient_name, quantity, measure = in_put.readline().split(' | ')
                structure_dict = {
                    'ingridient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure.strip()
                }
                structure_list.append(structure_dict)
            in_put.readline()
            cook_book[food_name] = structure_list
    all_products = []
    products = {}
    my_dict = {}
    for i in dishes:
        all_products.append(cook_book[i])
    for j in all_products:
        for now in j:
            if now['ingridient_name'] in products:
                products[now['ingridient_name']]['quantity'] += int(now['quantity']) * person_count
            else:
                my_dict['quantity'] = now['quantity'] * person_count
                my_dict['measure'] = now['measure']
                products[now['ingridient_name']] = my_dict
            my_dict = {}
    print(products)


get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3)
