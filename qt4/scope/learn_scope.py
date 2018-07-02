#!/usr/bin/env python3
#-*- coding : utf-8 -*-


class Test(object):
    
    a = 0  # 静态变量
    b = 1

    def __init__(self):
        self.add()    

    def add(self):
        print('a={}, b={}'.format(self.a, self.b))
        self.a += 1  # 类的成员变量,局部变量
        self.b += 1

Test.a = 1
Test.b = 1
test = Test()
print('a={}, b={}'.format(Test.a, Test.b))
print('a={}, b={}'.format(test.a, test.b))

