#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao
import logging

logging.basicConfig(
	filename='log.log',
	format='%(asctime)s-%(name)%s-%(levelname)s-%(module)s:%(message)s',
	datefmt='%Y-%m-%d %H:%M:%S %p',
	level=10
)
logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
logging.log(10,'log')