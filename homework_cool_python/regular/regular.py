import csv
import re


if __name__ == '__main__':
    my_list = []
    with open("phonebook_raw.csv", encoding='utf-8') as read_file:
        counter = 0
        headers = ''
        text = ''
        for i in csv.reader(read_file, delimiter=","):
            if counter == 0:
                headers = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                counter += 1
            else:
                my_string = f'{i[0]},{i[1]},{i[2]},{i[3]},{i[4]},{i[5]},' \
                            f'{i[6]}'
                text = text + my_string + '\n'
        pattern = r"([А-ЯЁ][а-яё]+)+\W([А-ЯЁ][а-яё]+)+\W([А-ЯЁ][а-яё]+)*," \
                  r"{1,3}([А-ЯЁа-яё]*),([^,]*),((\+7|8)[\D]{0,2}(\d{3})" \
                  r"[\D]{0,2}(\d{3})[\D]?(\d{2})[\D]?(\d{2})[\s\(]*" \
                  r"(доб\.\s\d{4})?\)?)*,(\S*)"
        subs = r"\1,\2,\3,\4,\5,+7(\8)\9-\10-\11 \12,\13"
        result = re.sub(pattern, subs, text)
        my_result = result.split(sep='\n')
        info = {}
        for i in my_result:
            if i == '':
                break
            one_string = i.split(',')
            if one_string[0] + ',' + one_string[1] not in info.keys():
                info[one_string[0] + ',' + one_string[1]] = [one_string[2],
                                                             one_string[3],
                                                             one_string[4],
                                                             one_string[5],
                                                             one_string[6]]
            else:
                counter = 2
                count = 0
                for k in info[one_string[0] + ',' + one_string[1]]:
                    if len(k) < len(one_string[counter]):
                        info[one_string[0] + ',' + one_string[1]][count]\
                            = one_string[counter]
                    counter += 1
                    count += 1
        my_list = [headers, ]
        for i in info:
            new_list = i.split(',')
            for k in info[i]:
                new_list.append(k)
            my_list.append(new_list)
        with open("phonebook.csv", "w", newline='', encoding='utf-8') as f:
            datawriter = csv.writer(f, delimiter=',')
            for i in my_list:
                datawriter.writerow(i)
