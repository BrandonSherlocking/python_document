fr = open('data.csv', 'r', encoding='utf-8')
ls = []
for line in fr:
    line = line.replace('\n', '')
    ls.append(line.split(','))
fr.close()
print(ls)
print('abadf{}{}{}{}'.format(*ls[0]))