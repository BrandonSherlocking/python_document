while 1:
    ls = input('xxx英文电子词典，请输入要查询的的单词\n \
    (输入添加、查询、退出进行操作)：')
    ks = []
    if ls == '添加':
        fname = input('请输入要添加的英文和中文解释（以逗号隔开）：')
        fo = open('EnglishDic.txt', 'a')
        lns = dict(fname)
        fo.write(lns)
        fo.close()
    elif ls == '查询':
        fname = input('请输入要查询的单词：')
        fo = open('EnglishDic.txt', 'r')
        lns = dict(fo)
        if fname in lns:
            print(lns[fname])
    elif ls == '退出':
        break
    else:
        print('你输入的有误:')
        break

