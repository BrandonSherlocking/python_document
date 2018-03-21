import os
# 获取需要重命名文件所在的文件夹
folder_name = input('请输入要重命名的文件夹：')
# 列出文件夹中的文件
file_names = os.listdir(folder_name)
os.chdir(folder_name)

# 重命名文件
for name in file_names:
    file_new_name = 'SHER出品' + name
    os.rename(name, file_new_name)
