import json
# 导入数据
path = 'I:\python文件\数据处理练习\example.txt'
fr = open(path)
# json转换成python格式，解码过程（json.dumps:与之相反，python转成json格式）
records = [json.loads(line) for line in fr]
# 统计‘tz’对应的值
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
print(time_zones[:20])


# 词频统计
def get_counts(sequence):
    counts = {}
    for x in sequence:
        counts[x] = counts.get(x, 0) + 1
    return counts


countsT = get_counts(time_zones)
num = countsT['America/New_York']
length = len(time_zones)
print('the America/New_York times is:{:>5}'.format(num))
print('the time_zones length is:{:>10}'.format(length))


# 统计默认前10词频
def top_counts(count_dict, n=10):
    value_key_pairs = list(count_dict.items())
    value_key_pairs.sort(key=lambda x: x[1], reverse=True)
    for i in range(n):
        word, count = value_key_pairs[i]
        print('{:<20}{:>15}'.format(word, count))
'''
另一种写法
def top_counts(count_dict, n=10):
    value_key_pairs = (count, tz) for tz, count in count_dict.items()
    value_key_pairs.sort()
    return value_key_pairs[-n:]
'''

'''
导入库的写法
from collexttions import Counter
counts = Counter(time_zones)
counts.most_common(10)
'''
top_counts(countsT)














