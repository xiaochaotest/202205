#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao

class School(object):
	#初始化学校人数为0
	member=0
	def __init__(self,name,addr):
		self.name=name
		self.addr=addr
		self.students=[]
		self.teachers=[]
		self.staffs=[]
	#学生注册
	def enroll(self,stu_obj):
		print('为学生%s提供注册。'%stu_obj.name)
		self.students.append(stu_obj)
	#老师注册
	def hire(self,staff_obj):
		self.staffs.append(staff_obj)
		print('雇佣新老师%s'%staff_obj.name)

class SchoolMember(object):

	def __init__(self,name,age,sex):
		self.name=name
		self.age=age
		self.sex=sex


	def tell(self):
		pass

class Teacher(SchoolMember):

	def __init__(self,name,age,sex,salary,cource):
		super(Teacher, self).__init__(name,age,sex)
		self.salary=salary
		self.cource=cource

	def tell(self):
		print(
			'''
			----info of Teacher:%s----
			Name:%s
			Age:%s
			sex:%s
			salary:%s
			cource:%s
			'''%(self.name,self.name,self.age,self.sex,self.salary,self.cource)
		)
	def teaching(self):
		print('%s老师是教%s课的'%(self.name,self.cource))

class Studens(SchoolMember):
	def __init__(self,name,age,sex,stu_id,grade):
		super(Studens, self).__init__(name,age,sex)
		self.stu_id=stu_id
		self.grade=grade

	def tell(self):
		print(
			'''
			----info of Student:%s----
			Name:%s
			Age:%s
			sex:%s
			Stu_id:%s
			Grade:%s
			'''%(self.name,self.name,self.age,self.sex,self.stu_id,self.grade)
		)

	def pay_tuition(self,amount):
		print('%s同学交了%s钱学费'%(self.name,amount))

school=School('平梁小学','巴中')

t1 = Teacher('oldboy',56,'M',50000,'英语')
t2 = Teacher('alex',36,'F',80000,'语文')

s1=Studens('张三',34,'女','2021001','英语')
s2=Studens('王五',14,'男','2021002','语文')

t1.tell()
s1.tell()

school.hire(t1)
school.enroll(s1)
school.enroll(s2)

print(school.staffs)
print(school.students)
#老师教课
school.staffs[0].teaching()

#学生缴费
for stu in school.students:
	stu.pay_tuition(5000)