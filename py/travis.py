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
        remove= input("Would you like to be removed from the system (y/n)?").strip().lower()
        if remove== "y":
            print(known_user)
            known_user.remove(name)
            print(known_user)
        elif remove=="n":
            print("Not a problem, i didn't want  you to leave anyway!")
            
    else:
        print("I dont't think we have met you yet {}".format(name))
        add_me=input("Would you like to be added to the system (y/n)? :").strip().lower()
        if add_me=="y":
            print(known_user)
            known_user.append(name)
            print(known_user)
        elif add_me =="n":
            print("Ok, you won't be added")
    