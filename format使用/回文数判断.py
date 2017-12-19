#本人代码
backnumber = input('请输入一串符号（数字或字母）：')
n = str(backnumber)
if n[0:-1] == n[-1:0:-1]:
    print('你输入的数字是回文数')
else:
    print('你输入的数字不是回文数')

# 大神代码
a = input('please input some word: ')
def is_palindrome(n):
    n = str(n)
    m = n[::-1]
    return n == m
if is_palindrome(a) is True:
    print('you input word is back word')
else:
    print('you input word is not back word')

