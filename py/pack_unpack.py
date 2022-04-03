'''
Created on Apr 2, 2022

@author: Joker
'''
num=[1,2,3,4,5]

def add(x,y):
    return x+y
add(10,10)
def adds(*num):
    total=0
    for number in num:
        total=total+number
    return(total)
a=adds(1,2,3,4,5,6,7,8,9)
print(a)
print(type(a))

def about(name,age,likes):
    sent="meet {} they are {} years old and they like {}".format(name,age,likes)
    return sent
dict={"name":"bob", "age":23,"likes":"python"}

def foo(**kwargs):
    for key,value in kwargs.items():
        print("{}:{}".format(key,value))


print(foo(huda="female", zim="male"))