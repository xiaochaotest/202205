#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao

import configparser
config=configparser.ConfigParser()
# config['DEFAULT']={'ServerAliveInterval':'45',
#                    'Comperssion':'yes',
#                    'ComperssionLevel':'9'
#                    }
#
# config['bibucket.org']={}
# config['bibucket.org']['User']='hg'
# config['topsecret.server.com']={}
# topsecret=config['topsecret.server.com']
# topsecret['Host port']='5022'
# topsecret['ForwardX11']='no'
# config['DEFAULT']['ForwardX11']='yes'
# with open('example.ini','w')as configfile:
# 	config.write(configfile)

	#读
print(config.defaults())
print(config.sections())#只打印节点
print(config.read('example.ini'))
print(config.sections())
print('bitbucket.org' in  config)
print(config['bibucket.org']['User'])
topsecret = config['topsecret.server.com']
print(topsecret['Host port'])

for key in config['bibucket.org']:print(key)


#增删改查
config = ConfigParser.ConfigParser()
config.read('i.cfg')

# ########## 读 ##########
# secs = config.sections()
# print secs
# options = config.options('group2')
# print options

# item_list = config.items('group2')
# print item_list

# val = config.get('group1','key')
# val = config.getint('group1','key')

# ########## 改写 ##########
# sec = config.remove_section('group1')
# config.write(open('i.cfg', "w"))

# sec = config.has_section('wupeiqi')
# sec = config.add_section('wupeiqi')
# config.write(open('i.cfg', "w"))


# config.set('group2','k1',11111)
# config.write(open('i.cfg', "w"))

# config.remove_option('group2','age')
# config.write(open('i.cfg', "w"))