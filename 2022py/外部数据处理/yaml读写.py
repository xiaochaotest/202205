#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao
import yaml

#打印出列表格式
print(yaml.load('''
 - Hesperiidae
 - Papilionidae
 - Apateloadidae
 - Epiplemidae
''',Loader=yaml.FullLoader))

#打印出字典
#打印出字典格式
print(yaml.load('''
'a': 1
''',Loader=yaml.FullLoader))

print(yaml.load(open('demo.yaml'), Loader=yaml.FullLoader))

#将字典转为yaml格式
print(yaml.dump({'a': [1,2]}))

#写入文件

with open('demo3.yaml','w')as f:
	yaml.dump(data={'a': [1,10,12]},stream=f)
