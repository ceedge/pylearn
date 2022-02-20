'''
Created on Feb 17, 2022

@author: Joker
'''

known_user = ["Alice", "Bob", "Dan", "Fred", "Harry", "Jim"]

print(len(known_user))

while True:
    print("Hi my name is Travis")
    name= input("What is your name? : ").strip().capitalize()
    if name in known_user:
        print("name recognised")
    else:
        print("name NOT  recognised")
    