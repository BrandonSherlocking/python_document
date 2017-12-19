import jieba
excludes = {'将军', '却说', '荆州', '二人', '不可', '不能', '如此', '商议',\
            '如何', '军士', '左右', '军马', '引兵', '次日', '大喜', '主公', '天下', '今日',\
            '于是', '不敢', '今日', '人马', '不知', '东吴', '魏兵', '陛下', '都督', '一人',\
            '汉中', '众将', '后主', '只见', '蜀兵', '大叫', '上马', '天子', '此人', '一面',\
            '先主', '太守', '后人', '背后', '何不', '城中', '忽报', '先锋', '然后', '大军',\
            '先生', '何故', '夫人', '不如', '令人', '赶来', '原来', '江东', '正是', '忽然',\
            '徐州', '成都', '下马'}
txt = open('I:\python文件\小作业\《三国演义》罗贯中.txt', 'r', encoding='UTF-8').read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == '诸葛亮' or word == '孔明曰':
        rword = '孔明'
    elif word == '关公' or word == '云长':
        rword = '关羽'
    elif word == '玄德' or word == '玄德曰':
        rword = '刘备'
    elif word == '孟德' or word == '丞相':
        rword = '曹操'
    else:
        rword = word
    counts[rword] = counts.get(rword, 0) + 1
for word in excludes:
    del(counts[word])
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(15):
    word, count = items[i]
    print('{0:<8}{1:>5}'.format(word, count))