#모듈, 재귀함수
'''
import Module

Module.func1()
Module.func2()
Module.func3()

'''
'''
from Module import *

func1()
func2()
func3()

'''

def count(num):
    if num >=1:
        print(num, end='')
        count(num-1)
    else:
        return


count(5)
count(10)
