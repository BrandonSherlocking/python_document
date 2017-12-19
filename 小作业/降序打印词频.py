receive = input('请输入一些东西:')
lire = list(receive)
counts = {}
for n in lire:
    counts[n] = counts.get(n, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for s in items:
    print(s)

