# Объединить списки преподавателей по всем курсам
def unic_name(mentors: list):
    all_list = []
    [all_list.extend(x) for x in mentors]
    # Отделить имя от фамилии
    all_names_list = [x.split(" ")[0].strip() for x in all_list]
    # Убрать дубли при помощи множеств
    all_names_set = set(all_names_list)
    # Тренажёру нужен постояннный порядок, поэтому сортируем имена по алфавиту
    all_names_sorted = sorted(list(all_names_set))
    return all_names_sorted


def top_3_name(mentors: list):
    # Объединить списки преподавателей по всем курсам
    all_list = []
    [all_list.extend(x) for x in mentors]
    # Отделить имя от фамилии
    all_names_list = [x.split(" ")[0].strip() for x in all_list]
    # Убрать дубли при помощи множеств
    all_names_set = set(all_names_list)
    all_modern_names_list = list(all_names_set)
    all_modern_names_list.sort()

    # Подсчитываем встречаемость каждого имени
    popular = [[all_names_list.count(x), x] for x in all_modern_names_list]
    # Сортируем по убыванию встречаемости
    popular.sort(key=lambda x: x[0], reverse=True)
    # Выводим топ-3 имён
    top_3 = [f"{str(x[1])}: {str(x[0])} раз(а)" for x in popular[:3]]
    return top_3


def calc_pair(mentors: list, courses: list):
    # Делаем список списков имён
    mentors_names = [[y.split(" ")[0].strip() for y in x] for x in mentors]

    pairs = []
    # Попарное сравнение списков преподавателей на курсах. Каждую новую пару запоминаем для исключения повторов.
    # Пары храним как множества, а не как списки, потому что для множеств не важен порядок элементов
    for id1 in range(len(mentors_names)):
        for id2 in range(len(mentors_names)):
            if id1 == id2:
                continue
            intersection_set = set(mentors_names[id1]) & set(
                mentors_names[id2])
            if len(intersection_set) > 0:
                pair = {courses[id1], courses[id2]}
                if pair not in pairs:
                    pairs.append(pair)
                    # Тренажёру нужен постояннный порядок, поэтому сортируем имена по алфавиту
                    all_names_sorted = sorted(list(intersection_set))
                    return all_names_sorted
