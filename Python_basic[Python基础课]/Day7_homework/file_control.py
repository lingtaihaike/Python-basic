import os

os.chdir('test')

print('文件中包含"qytang"关键字的文件为:')
for file_or_dir in os.listdir():
    if os.path.isfile(file_or_dir) is True:
        if 'qytang' in open(file_or_dir).read():
            print(file_or_dir)
            os.remove(file_or_dir)
        else:
            os.remove(file_or_dir)
    else:
        os.removedirs(file_or_dir)
        continue


os.chdir('..')
os.removedirs('test')