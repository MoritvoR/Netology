import psycopg2


class DB:
    def __init__(self, name_db: str, name_user: str, password_user: str):
        self.name_db = name_db
        self.name_user = name_user
        self.password_user = password_user

    def create_db(self, connect):
        """Create table in database"""
        with connect.cursor() as curva:
            curva.execute("""DROP TABLE IF EXISTS client CASCADE;
            DROP TABLE IF EXISTS phone CASCADE;
        
            CREATE TABLE client(client_id SERIAL PRIMARY KEY,
            name VARCHAR(32) NOT NULL,
            surname VARCHAR(64) NOT NULL,
            email VARCHAR(64) NOT NULL);
        
            CREATE TABLE phone(phone_id SERIAL PRIMARY KEY,
            phone VARCHAR(16) NOT NULL,
            client_id INT NOT NULL REFERENCES client(client_id));
            """)
            connect.commit()
            print('Таблицы успешно созданы.')


class Client:
    def __init__(self, name: str, surname: str, email: str):
        self.name = name
        self.surname = surname
        self.email = email

    def add_client(self, connect):
        """Create new client"""
        with connect.cursor() as curva:
            curva.execute("""INSERT INTO client(name, surname, email)
            VALUES (%s, %s, %s) RETURNING client_id; 
            """, (self.name, self.surname, self. email))
            client_id = curva.fetchone()[0]
            counter = int(input('Сколько телефонов у клиента {}? (введите '
                                'число): '.format(self.name)))
            for i in range(counter):
                phones = input('Введите {}-ый/ой/ий телефон '
                               'клиента:'.format(i + 1))
                curva.execute("""INSERT INTO phone(phone, client_id)
                VALUES (%s, %s)""", (phones, client_id))
                connect.commit()
            connect.commit()
            print('Клиент успешно добавлен.')

    def add_phone(self, connect):
        """Create new client's phone."""
        with connect.cursor() as curva:
            curva.execute("""SELECT client_id
                        FROM client
                        WHERE name=%s AND surname=%s""", (self.name,
                                                          self.surname))
            client_id = curva.fetchone()
            if client_id is None:
                print("Такого клиента не существует.")
            else:
                counter = int(input('Сколько телефонов у клиента? (введите '
                                    'число): '))
                for i in range(counter):
                    phones = input('Введите {}-ый/ой/ий телефон '
                                   'клиента:'.format(i + 1))
                    curva.execute("""INSERT INTO phone(phone, client_id)
                                VALUES (%s, %s)""", (phones, client_id))
                connect.commit()
                print('Телефон успешно добавлен.')

    def __input_info__(self):
        name = input('Введите новое имя: ')
        surname = input('Введите новую фамилию: ')
        email = input('Введите новый email: ')
        return name, surname, email

    def update_client(self, connect):
        """Update information about client"""
        name, surname, email = self.__input_info__()
        with connect.cursor() as curva:
            curva.execute("""UPDATE client
            SET name=%s, surname=%s, email=%s
            WHERE name=%s AND surname=%s AND email=%s
            """, (name, surname, email, self.name, self.surname, self.email))
        self.name = name
        self.surname = surname
        self.email = email
        connect.commit()
        print('Данные успешно обновлены.')

    def delete_phones(self, connect):
        """Delete client's phone."""
        with connect.cursor() as curva:
            curva.execute("""SELECT client_id
            FROM client
            WHERE name=%s AND surname=%s""", (self.name, self.surname))
            client_id = curva.fetchone()
            curva.execute("""DELETE FROM phone
            WHERE client_id=%s""", (client_id, ))
            conn.commit()
            print('Телефоны успешно удалены.')

    def delete_client(self, connect):
        """Delete information about client."""
        with connect.cursor() as curva:
            curva.execute("""SELECT client_id
            FROM client
            WHERE name=%s AND surname=%s""", (self.name, self.surname))
            client_id = curva.fetchone()
            curva.execute("""DELETE FROM phone
            WHERE client_id=%s""", (client_id, ))
            curva.execute("""DELETE FROM client
            WHERE client_id=%s""", (client_id, ))
            connect.commit()
            print('Удаление клиента прошло успешно.')


def search_client(connect, name=None, surname=None, email=None, phone=None):
    """Search information in database about client"""
    with connect.cursor() as curva:
        if phone is not None:
            curva.execute("""SELECT client_id
            FROM phone
            WHERE phone=%s""", (phone, ))
            client_id = curva.fetchone()
            curva.execute("""SELECT *
            FROM client
            WHERE client_id=%s""", (client_id, ))
            my_list = curva.fetchone()
            print('client id = ', my_list[0])
            print('name = ', my_list[1])
            print('surname = ', my_list[2])
            print('email = ', my_list[3])
        elif email is not None:
            curva.execute("""SELECT *
            FROM client
            WHERE email=%s""", (email, ))
            my_list = curva.fetchone()
            print('client id = ', my_list[0])
            print('name = ', my_list[1])
            print('surname = ', my_list[2])
            print('email = ', my_list[3])
        elif name is not None:
            if surname is not None:
                curva.execute("""SELECT *
                FROM client
                WHERE name=%s AND surname=%s""", (name, surname))
                my_list = curva.fetchone()
                print('client id = ', my_list[0])
                print('name = ', my_list[1])
                print('surname = ', my_list[2])
                print('email = ', my_list[3])
            else:
                curva.execute("""SELECT *
                FROM client
                WHERE name=%s""", (name, ))
                my_list = curva.fetchall()
                for i in my_list:
                    print('client id = ', i[0])
                    print('name = ', i[1])
                    print('surname = ', i[2])
                    print('email = ', i[3])
        elif surname is not None:
            curva.execute("""SELECT *
            FROM client
            WHERE surname=%s""", (surname, ))
            my_list = curva.fetchall()
            for i in my_list:
                print('client id = ', i[0])
                print('name = ', i[1])
                print('surname = ', i[2])
                print('email = ', i[3])


if __name__ == '__main__':
    db_name = input('Введите имя базы данных: ')
    user_name = input('Введите имя пользователя: ')
    password = input('Введите пароль для пользователя: ')
    my_db = DB(db_name, user_name, password)
    conn = psycopg2.connect(database=my_db.name_db, user=my_db.name_user,
                            password=my_db.password_user)

    my_db.create_db(conn)

    pider = Client('Pider', 'Parker', 'parker@pidera.net')
    pider.add_client(conn)
    dre = Client('Doctor', 'Dre', 'doctor@dre.com')
    dre.add_client(conn)
    mim = Client('Ponto', 'Mim', 'ponto@mim.ru')
    mim.add_client(conn)

    mim.add_phone(connect=conn)

    dre.update_client(connect=conn)

    dre.delete_phones(conn)

    dre.delete_client(conn)

    search_client(conn, 'Pider')

    conn.close()
