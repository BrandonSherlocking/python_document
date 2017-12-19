def judgeWord():
    while True:
        rescive = input('请输入一些东西(输入q或quit退出)：')
        lsre = list(rescive)
        if rescive == 'q' or rescive == 'quit':
            break
        elif len(set(lsre)) == len(lsre):
            print('你输入的字符没有重复')
        else:
            print('True')
judgeWord()



