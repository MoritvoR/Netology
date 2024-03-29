from pytest import mark
import data_collection


@mark.parametrize('mentors,expected',
                  [
                      (
                          [["Евгений Шмаргунов", "Олег Булыгин",
                            "Дмитрий Демидов", "Кирилл Табельский",
                            "Александр Ульянцев"],
                           ["Филипп Воронов", "Анна Юшина", "Иван Бочаров",
                            "Анатолий Корсаков"]],
                          ["Александр", "Анатолий", "Анна", "Дмитрий",
                           "Евгений", "Иван", "Кирилл", "Олег", "Филипп"]
                      ),
                      (
                          [["Анна Аннаньевна", "Павел Павеленко"],
                           ["Олег Ольков", "Яйцеслав Вафлевин"]],
                          ["Анна", "Олег", "Павел", "Яйцеслав"]
                      )
                  ])
def test_unic_name(mentors, expected):
    result = data_collection.unic_name(mentors)
    assert expected == result


@mark.parametrize('mentors,expected',
                  [
                      (
                          [["Евгений Шмаргунов", "Олег Булыгин",
                            "Дмитрий Демидов", "Кирилл Табельский",
                            "Александр Ульянцев", "Александр Бардин"],
                           ["Вадим Ерошевичев", "Тимур Сейсембаев",
                            "Максим Батырев", "Никита Шумский",
                            "Алексей Степанов", "Денис Коротков",
                            "Антон Глушков"]],
                          ['Александр: 2 раз(а)', 'Алексей: 1 раз(а)',
                           'Антон: 1 раз(а)']
                      ),
                      (
                          [["Евгений Шмаргунов", "Олег Булыгин",
                            "Александр Бардин", "Александр Иванов",
                            "Кирилл Табельский", "Александр Ульянцев",
                            "Роман Гордиенко", "Адилет Асканжоев",
                            "Александр Шлейко", "Алена Батицкая"],
                           ["Владимир Чебукин", "Эдгар Нуруллин",
                            "Евгений Шек", "Валерий Хаслер",
                            "Татьяна Тен", "Александр Фитискин",
                            "Александр Шлейко", "Алена Батицкая"]],
                          ['Александр: 6 раз(а)', 'Алена: 2 раз(а)',
                           'Евгений: 2 раз(а)']
                      )
                  ])
def test_top_3_name(mentors, expected):
    result = data_collection.top_3_name(mentors)
    assert expected == result


@mark.parametrize('mentors,courses,expected',
                  [
                      ([["Евгений Шмаргунов", "Олег Булыгин",
                         "Дмитрий Демидов", "Кирилл Табельский",
                         "Александр Ульянцев", "Александр Бардин"],
                        ["Вадим Ерошевичев", "Тимур Сейсембаев",
                         "Максим Батырев", "Никита Шумский",
                         "Алексей Степанов", "Денис Коротков",
                         "Антон Глушков"]],
                       ["Python-разработчик с нуля", "Java-разработчик с нуля",
                        "Fullstack-разработчик на Python",
                        "Frontend-разработчик с нуля"],
                       None
                       ),
                      ([
                          ["Евгений Шмаргунов", "Роман Гордиенко"],
                          ["Филипп Воронов", "Сергей Сердюк",
                           "Павел Дерендяев"],
                          ["Евгений Шмаргунов", "Олег Булыгин",
                           "Роман Гордиенко"],
                          ["Владимир Чебукин", "Эдгар Нуруллин",
                           "Павел Дерендяев", "Роман Гордиенко"]
                       ],
                       ["Python-разработчик с нуля",
                        "Java-разработчик с нуля",
                        "Fullstack-разработчик на Python",
                        "Frontend-разработчик с нуля"],
                       ['Евгений', 'Роман'])
                  ]
                  )
def test_calc_pair(mentors, courses, expected):
    result = data_collection.calc_pair(mentors, courses)
    assert expected == result
