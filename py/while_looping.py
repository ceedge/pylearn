'''
Created on Mar 19, 2022

@author: Joker
'''


num=1
while num <= 1500:
    if num%2!=0:
        print(num)
    num= num +1  

L=[]
while len(L)<3:
    new_name=input("Please add a new number:").strip().capitalize()
    L.append(new_name)

print("Sorry the list is full", L)
    