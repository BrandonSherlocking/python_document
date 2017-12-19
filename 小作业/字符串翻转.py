while True:
    def reverse(s):
        if s == '':
            return s
        else:
            return reverse(s[1:]) + s[0]
    print('输入 q 或 quit 退出')
    st = input('请输入一串字符：')
    if st == 'q' or st == 'quit':
        break
    print(reverse(st))
    print()




