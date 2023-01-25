directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }
number_of_document = input('Введите номер документа: ')
for key, value in directories.items():
    if number_of_document in value:
        print(key)
print('Такого номера документа нет в списке')