
# 直接打印
print('网站名：{name},地址：{url}'.format(name='菜鸟教程', url='www.runoob.com'))

# 通过字典设置参数
site = {'name': '菜鸟教程', 'url': 'www.runoob.com'}
print('网站名：{name},地址：{url}'.format(**site))

# 通过列表索引设置参数
My_list = ['菜鸟教程', 'www.runoob.com']
print('网站名：{0[0]},地址：{0[1]}'.format(My_list))  # 0是可选的
