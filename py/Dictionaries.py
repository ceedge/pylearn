'''
Created on Mar 13, 2022

@author: Joker
'''

stu={}
stu={"alice":25, "bob":27,"dan":17, "emma":22}

print(stu)
print(stu["dan"])

stu["fred"]=25

print(stu)

stu["alice"]=26

del stu["fred"]

print(stu.keys())
print(stu.items())