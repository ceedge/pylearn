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
        print("Hello {}!".format(name))
        remove= input("Would you like to be removed from the system (y/n)?").lower()
        if remove== "y":
            print(known_user)
            known_user.remove(name)
            print(known_user)
            
    else:
        print("I dont't think we have met you yet{}".format(name))
        add_me=input("Would you like to be added to the system (y/n)? :")
        
    