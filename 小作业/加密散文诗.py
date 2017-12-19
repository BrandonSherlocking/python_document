s = '''
  became a searcher,wanting to find out who I was and what made me unique. 
  My view of myself was changing. I wanted a solid base to start from. 
  I started to resist3 pressure to act in ways that 
  I didn’t like any more,and I was delighted by who I really was. 
  I came to feel much more sure that no one can ever take my place.
　Each of us holds a unique place in the world. 
  You are special,no matter what others say or what you may think. 
  So forget about being replaced. You can’t be.'''
d ={}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13)%26 + c)
print(''.join([d.get(c, c)for c in s]))