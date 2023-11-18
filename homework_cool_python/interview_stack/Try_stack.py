from Stack import Stack


my_stack = Stack(input('Введите строку: '))

if my_stack.size() % 2 == 0:
    info_set = {'(': 0, '[': 0, '{': 0, ')': 0, ']': 0, '}': 0}
    for i in range(my_stack.size()):
        info_set[my_stack.pop()] += 1
    if info_set['('] == info_set[')'] \
            and info_set['['] == info_set[']'] \
            and info_set['{'] == info_set['}']:
        print('Сбалансированно')
    else:
        print('Несбалансированно')
else:
    print('Несбалансированно')
