#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao

import shutil
import os

f =os.path.dirname(os.path.dirname(__file__))
s=os.path.join(os.path.dirname(os.path.dirname(__file__)),'day02','test1.txt')
print(s)
# with open(s,'r')as f1:
# 	print(f1.read())
#将文件拷贝到另一个文件中
# a=open('test.txt',encoding='utf-8')
#
# a1 = open('test1.txt','w',encoding='utf-8')
# shutil.copyfileobj(a,a1)
#
# shutil.copyfile(s,'test2.txt')

#shutil对压缩包的处理是调用zipfile和tarfile两个模块来进行的

#将文件打包放置到当前程序目录
ret=shutil.make_archive('www','gztar',root_dir=f)
#将文件打包放置到其他程序目录
ret1=shutil.make_archive(s,'gztar',root_dir=f)


#压缩
# import zipfile
# z=zipfile.ZipFile('day02.zip','w')
# z.write(f)
# print('------')
# z.write(s)
# z.close()
# #解压
# z = zipfile.ZipFile('day02.zip','r')
# z.extractall()
# z.close()



# import tarfile
#
# # 压缩
# tar = tarfile.open('your.tar','w')
# tar.add('/Users/wupeiqi/PycharmProjects/bbs2.zip', arcname='bbs2.zip')
# tar.add('/Users/wupeiqi/PycharmProjects/cmdb.zip', arcname='cmdb.zip')
# tar.close()
#
# # 解压
# tar = tarfile.open('your.tar','r')
# tar.extractall()  # 可设置解压地址
# tar.close()