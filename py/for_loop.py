'''
Created on Mar 20, 2022

@author: Joker
'''

for number in range(1,501):
    print(number)

for letter in "abcdefli" :
    print(letter)


vowels=0
for letters in "Hello":
    if letters.lower() in "aeiou" :
        vowels=vowels+1
    elif letters==" ":
        pass
    else:
        