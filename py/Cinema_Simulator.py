'''
Created on Mar 18, 2022

@author: Joker
'''
Films={
    "Finding Dory":[3,5],
    "Bournce":[18,5],
    "Tarzan":[15,5],
    "Ghost Busters":[12,5]
    }

while True:
    choice= input("what film would you like to watch? :").strip().title()
    if choice in Films:
        age=int(input("How old are you? :").strip())
        
        #check user age
        if age>=Films[choice][0]:
            # check enough seats
            if Films[choice][1]>0:
                print("Enjoy the film!")
                Films[choice][1]=Films[choice][1]-1
        else:
            print("You are too young to see this film!")
    else:
        print(" We dont't have that film...")