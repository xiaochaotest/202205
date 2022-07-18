#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao
import xml.etree.ElementTree as ET

tree = ET.parse('xmltest.xml')
root=tree.getroot()
print(root.tag)#打印标签名

#遍历整个xml文档
for child in root:
	print(child.tag,child.attrib)#打印第二层tag及属性
	for i in child:
		print(i.tag,i.text,i.attrib)#打印第三层的tag，内容，及属性

#只遍历year节点
for node in root.iter('year'):
	print(node.tag,node.text)

#修改

for s in root.iter('year'):
	new_year=int(s.text)+1
	s.text=str(new_year)
	s.set("updated",'alexs')#修改属性
tree.write('xmltest.xml')

#删除
for county in root.findall('county'):
	rank = int(county.find('rank').text)
	if rank > 50:
		root.remove(county)
tree.write('xmltets.xml')


#自己创建xml


new_xml = ET.Element('namelist')
name=ET.SubElement(new_xml,'name',attrib={"enrolled":'yes'})
age = ET.SubElement(name,'age',attrib={"checked":'no'})
sex=ET.SubElement(name,'sex')
sex.text=33
name2=ET.SubElement(new_xml,'name',attrib={'enrolled':'no'})
age = ET.SubElement(name2,'age')
age.text=19
et=ET.ElementTree(new_xml)#生成文挡对象
et.write('test.xml',encoding='utf-8',xml_declaration=True)
ET.dump(new_xml)#打印生成格式















