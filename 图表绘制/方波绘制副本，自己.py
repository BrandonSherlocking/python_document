import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

labels = ['China', 'Swiss', 'USA', 'UK', 'Laos', 'Spain']
X = [222, 42, 455, 664, 454, 334]
def trans(n):
    if n == 'China':
        return 0.1
    else:
        return 0
a = []
exp1 = list(map(trans, labels))
d = [0.1, 0, 0, 0, 0.1, 0]
fig = plt.figure()
plt.pie(X, labels=labels, explode=exp1, autopct='%1.2f%%')  # 画饼图（数据，数据对应的标签，百分数保留两位小数点）
plt.title("Pie chart")

plt.show()