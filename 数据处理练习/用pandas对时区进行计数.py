import json
# 导入
from pandas import DataFrame, Series
import pandas as pd
import numpy as np
# 导入数据
path = 'I:\python文件\数据处理练习\example.txt'
fr = open(path)
# json转换成python格式，解码过程（json.dumps:与之相反，python转成json格式）
records = [json.loads(line) for line in fr]
# 统计‘tz’对应的值
time_zones = [rec['tz'] for rec in records if 'tz' in rec]


frame = DataFrame(records)
# 缺失值代替: fillna函数
clean_tz = frame['tz'].fillna('Missing')
# 空字符串，布尔型数组索引
clean_tz[clean_tz == ''] = 'Unknown'
# 统计前10
tz_counts = clean_tz.value_counts()
print(tz_counts[:10])
# 用pylab模式打开shell：ipython --pylab
tz_counts[:10].plot(kind='barh', rot=0)

# 提取agent信息
results = Series([x.split()[0] for x in frame.a.dropna()])
print(results[:5])
print(results.value_counts()[:8])
# 按windows和非windows提取
cframe = frame[frame.a.notnull()]
operating_system = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'not Windows')
print(Series(operating_system[:5]))
# 根据时区和系统对数据进行分组
by_tz_os = cframe.groupby(['tz', operating_system])
agg_counts = by_tz_os.size().unstack().fillna(0)
print(agg_counts[:10])
