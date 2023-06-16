import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from model_SQLAlchemy import create_tables, Publisher, Sale, Shop, Stock, Book


print('Добро пожаловать!')
name_driver = input('Введите имя драйвера подключения: ')
name_login = input('Введите логин пользователя: ')
password = input('Введите пароль пользователя: ')
host_name = input('Введите имя хоста: ')
server_port = input('Введите порт сервера: ')
name_db = input('Введите имя базы данных: ')

DSN = f'{name_driver}://{name_login}:{password}@{host_name}:' \
      f'{server_port}/{name_db}'

engine = sq.create_engine(DSN)

Session = sessionmaker(bind=engine)

if input('Необходимо создать таблицы?(да\нет): ').lower() == 'да':
    create_tables(engine)

if input('Необходимо заполнить таблицы тестовыми данными?(да/нет): ').lower()\
        == 'да':
    session = Session()
    publisher1 = Publisher(publisher_id=1, name='Reilly')
    publisher2 = Publisher(publisher_id=2, name='Pearson')
    publisher3 = Publisher(publisher_id=3, name='Microsoft Press')
    publisher4 = Publisher(publisher_id=4, name='No starch press')

    book1 = Book(title='Programming Python, 4th Edition', id_publisher=1)
    book2 = Book(title='Learning Python, 4th Edition', id_publisher=1)
    book3 = Book(title='Natural Language Processing with Python',
                 id_publisher=1)
    book4 = Book(title='Hacking: The Art of Exploitation',
                 id_publisher=4)
    book5 = Book(title='Modern Operating Systems', id_publisher=2)
    book6 = Book(title='Code Complete: Second Edition', id_publisher=3)

    shop1 = Shop(name='Labirint')
    shop2 = Shop(name='OZON')
    shop3 = Shop(name='Amazon')

    sale1 = Sale(price='50.05', date_sale='2018-10-25T09:45:24.552Z',
                 count=16, id_stock=1)
    sale2 = Sale(price='50.05', date_sale='2018-10-25T09:51:04.113Z',
                 count=10, id_stock=3)
    sale3 = Sale(price='10.50', date_sale='2018-10-25T09:52:22.194Z',
                 count=9, id_stock=6)
    sale4 = Sale(price='16.00', date_sale='2018-10-25T10:59:56.230Z',
                 count=5, id_stock=5)
    sale5 = Sale(price='16.00', date_sale='2018-10-25T10:59:56.230Z',
                 count=5, id_stock=9)
    sale6 = Sale(price='16.00', date_sale='2018-10-25T10:59:56.230Z',
                 count=1, id_stock=4)

    stock1 = Stock(id_book=1, id_shop=1, count=34)
    stock2 = Stock(id_book=2, id_shop=1, count=30)
    stock3 = Stock(id_book=3, id_shop=1, count=0)
    stock4 = Stock(id_book=5, id_shop=2, count=40)
    stock5 = Stock(id_book=6, id_shop=2, count=50)
    stock6 = Stock(id_book=4, id_shop=3, count=10)
    stock7 = Stock(id_book=6, id_shop=3, count=10)
    stock8 = Stock(id_book=1, id_shop=2, count=10)
    stock9 = Stock(id_book=1, id_shop=3, count=10)
    session.add_all([publisher1, publisher2, publisher3, publisher4, book1,
                     book2, book3, book4, book5, book6, shop1, shop2, shop3,
                     stock1, stock2, stock3, stock4, stock5, stock6, stock7,
                     stock8, stock9, sale1, sale2, sale3, sale4, sale5, sale6])
    session.commit()
    session.close()

i = int(input('Введите, что необходимо сделать: \n'
          '1 - вывести проданные книги по имени издателя\n'
          '2 - вывести проданые книги по идентификатору издателя\n'
          '0 - выйти из программы\n'))
Session = sessionmaker(bind=engine)
session = Session()
while i != 0:
    if i == 1:
        name_pub = input('Введите имя издателя: ')
        query = session.query(Publisher.publisher_id,
                              Book.title, Shop.name,
                              Sale.price,
                              Sale.date_sale)\
            .filter(Publisher.name.like(name_pub))
        query = query.join(Book, Publisher.publisher_id == Book.id_publisher)
        query = query.join(Stock, Book.book_id == Stock.id_book)
        query = query.join(Shop, Stock.id_shop == Shop.shop_id)
        query = query.join(Sale, Stock.stock_id == Sale.id_stock)
        query = query.all()

        counter = 0
        my_max = len(query[0][1])
        for i in query:
            if my_max <= len(i[1]):
                my_max = len(i[1])
        for i in query:
            if len(i[1]) < my_max:
                counter = my_max - len(i[1]) + 1
                print(i[1], end=' ' * counter)
                print(' | ', i[2], ' | ', i[3], ' | ', i[4])
            else:
                print(i[1], ' | ', i[2], ' | ', i[3], ' | ', i[4])
    elif i == 2:
        ident = int(input('Введите идентификатор издателя: '))
        query = session.query(Publisher.publisher_id,
                              Book.title, Shop.name,
                              Sale.price,
                              Sale.date_sale) \
            .filter(Publisher.publisher_id == ident)
        query = query.join(Book, Publisher.publisher_id == Book.id_publisher)
        query = query.join(Stock, Book.book_id == Stock.id_book)
        query = query.join(Shop, Stock.id_shop == Shop.shop_id)
        query = query.join(Sale, Stock.stock_id == Sale.id_stock)
        query = query.all()

        counter = 0
        my_max = len(query[0][1])
        for i in query:
            if my_max <= len(i[1]):
                my_max = len(i[1])
        for i in query:
            if len(i[1]) < my_max:
                counter = my_max - len(i[1]) + 1
                print(i[1], end=' ' * counter)
                print(' | ', i[2], ' | ', i[3], ' | ', i[4])
            else:
                print(i[1], ' | ', i[2], ' | ', i[3], ' | ', i[4])
    i = int(input('Введите, что необходимо сделать: \n'
                  '1 - вывести проданные книги по имени издателя\n'
                  '2 - вывести проданые книги по идентификатору издателя\n'
                  '0 - выйти из программы\n'))


session.close()
