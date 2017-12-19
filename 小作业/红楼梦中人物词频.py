import jieba
excludes = {'什么', '一个', '我们', '如今', '你们', '不能', '如此', '商议', \
            '说道', '知道', '起来', '这里', '姑娘', '出来', '他们', '众人', \
            '奶奶', '自己', '一面', '太太', '姑娘', '只见', '两个', '怎么', \
            '没有', '不是', '不知', '这个', '听见', '这样', '那里', '进来'}

txt = open('I:\python文件\小作业\《红楼梦》.txt', 'r', encoding='UTF-8').read()
words = jieba.lcut(txt)
counts = {}

for word in words:
    if len(word) == 1:
        continue
   # elif word == '诸葛亮' or word == '孔明曰':
       # rword = '孔明'
   # elif word == '关公' or word == '云长':
       # rword = '关羽'
   # elif word == '玄德' or word == '玄德曰':
      #  rword = '刘备'
   # elif word == '孟德' or word == '丞相':
       # rword = '曹操'
    else:
        #rword = word
        counts[word] = counts.get(word, 0) + 1
for word in excludes:
    del(counts[word])
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(20):
    word, count = items[i]
    print('{0:<8}{1:>5}'.format(word, count))