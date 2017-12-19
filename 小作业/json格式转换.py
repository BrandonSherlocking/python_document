import json
fr = open('data.csv', 'r', encoding='utf-8')
ls = []
for line in fr:
    line = line.replace('\n', '')
    ls.append(line.split(','))
fr.close()
fw = open('data.json', 'w', encoding='utf-8')
for i in range(1, len(ls)):
    ls[i] = dict(zip(ls[0], ls[i]))
json.dump(ls[1:], fw, sort_keys=True, indent=4, ensure_ascii=False)
fw.close()
