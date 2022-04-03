'''
Created on Mar 21, 2022

@author: Joker
'''
student={
    "male":["tom","charles", "harry", "frank"],
    "female":["sarah","hana", "emily", "liz"]
    }

for key in student.keys():
    print(key)
    print(student[key])
    for name in student[key]:
        if "a" in name:
            print(name)