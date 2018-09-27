#-*- coding: utf-8 -*-
class Employee:
    "所有员工的基类"
    emCount = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.emCount += 1
    def displayCount(self):
        print 'Total employee is %d' % Employee.emCount
    def displayemployee(self):
        print 'employee name is %s' % self.name , ' salary is %d' % self.salary


em1 = Employee('zhangsan',5000)
em2 = Employee('lisi',10000)
em1.age = 25
em2.age = 27
hasattr(em1, 'age')
em1.displayemployee()
em2.displayemployee()
em1.displayCount()

