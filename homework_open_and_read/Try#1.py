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
                'quantity': quantity,
                'measure': measure
            }
            structure_list.append(structure_dict)
        in_put.readline()
        cook_book[food_name] = structure_list
print(cook_book)


