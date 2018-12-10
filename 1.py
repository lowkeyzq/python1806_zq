#!/usr/bin/env python3
# -*- coding: utf-8 -*-

    #1.编写一个从 1 加到 end 的当型循环。变量 end 的值由键盘输入。假如输入 end的值为 6，则代码输出的结应该是 21，也就是 1+2+3+4+5+6 的结果（不要用sum 作为变量，因为它是内置函数）
'''
def fun(end):
    x = 1
    y = 0
    while x <= end:
        y += x
        x += 1
    print(y)

def fun(end):
    y = 0
    for x in range(1,end+1):
        y += x
    print(y)
end = int(input('输入:'))
fun(end)
'''
    #2从键盘输入一个整数，判断该数字能否被 2 和 3 同时整除，能否被 2 整除，能否被 3 整除，不能被 2 和 3 整除。输出相应信息
'''
def fun(x):
    if x % 2 == 0 and x % 3 ==0:
        print('能被2和3整除')
    elif x % 2 == 0:
        print('能被2整除')
    elif x % 3 ==0:
        print('能被3整除')
    else:
        print('NO能被2和3整除')
    return 0
x = int(input('输入:'))
fun(x)
'''
    #3 一个数如果恰好等于它的因子之和，这个数就称为“完数”，例如， 6 的因子为 1、 2、 3，而 6=1+2+3，因此 6 是“完数”。编程序找出 1000 之内的所有完数，并按下面的格式输出其因子：
'''
for x in range(1,1001):
    l = []
    for y in range(1,x):
        if x % y == 0:
            l.append(y)
    if sum(l) == x:
        print('%s是完数'%x,l)
'''
    #4打印出所有的“水仙花数”，所谓“水仙花数”是指一个 3 位数，其各位数字立方和等于该数本身。例如， 153 是一个水仙花数，因为 153=13+53+33。
'''
import math
for i in range(100, 1000):
    x = math.floor(i/100)  
    y = math.floor((i - x*100)/10)
    z = i - math.floor(i/10) *10
    if i == x**3 + y**3 + z**3:
        print('%s是水仙花数'%i)
'''
    #5输出 1~100 之间不能被 7 整除的数，每行输出 10 个数字，要求应用字符串格式化方法（任何一种均可） 美化输出格式。 输出效果为：

def fun(num):
    l = []
    for x in range(1,num+1):
        if x%7 != 0:
            l.append(x)
    z = 0
    m = 0
    for y in range(1,len(l)):
        if y%10 == 0:
            z = str(l[y-10:y]) 
            print(z.center(60,'*'))
            m += 1
    print(str(l[m*10:]).center(60,'*'))
    
fun(100)
    #6请输入颜值分:
    #假如你的身高大于180 并且身价大于1000000 并且颜值大于99分 就可以是高富帅
    #假如身价大于1000000 并且颜值大于99分 就可以是富帅
    #假如颜值大于99分 就可以是帅
    #假如你的身高小于160并且身价小于100并且颜值小于60分 就可以是矮穷矬
'''
def person(height,worth,level):
    if height >180 and worth >1000000 and level > 99:
        print('你是高富帅')
    elif worth >1000000 and level > 99:
        print('你是富帅')
    elif level > 99:
        print('你只是帅')
    else:
        print('你是矮矬穷')
person(192,1000,102)
''' 
    #7小明身高175，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
    #低于18.5：过轻
    #18.5-25：正常
    #25-28：过重
    #28-32：肥胖
    #高于32：严重肥胖
'''
def student(height,weight):
    bmi = weight/(height/100)**2
    if bmi >28 and bmi <= 32:
        print('肥胖')
    elif bmi >25 and bmi <= 28:
        print('过重')
    elif bmi >18.5 and bmi <= 25:
        print('正常')
    elif bmi > 0 and bmi <= 18.5:
        print('过轻')
    else:
        print('严重肥胖')
    
student(175,80.5)
    '''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
