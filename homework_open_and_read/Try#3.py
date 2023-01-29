size = {}
content = {}
for i in range(1, 4):
    with open('%s.txt' % i, 'r', encoding='utf-8') as file_txt:
        read_file = file_txt.readlines()
        size['%s.txt' % i] = len(read_file)
        content['%s.txt' % i] = read_file
with open('out_put.txt', 'w', encoding='utf-8') as out_put:
    for now in sorted(size, key=size.get):
        print(now, file=out_put)
        print(size[now], file=out_put)
        for i in content[now]:
            print(i, file=out_put, end='')
    