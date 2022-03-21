'''
Created on Mar 20, 2022

@author: Joker
'''

for number in range(1,501):
    print(number)

for letter in "abcdefli" :
    print(letter)

word= input("please type a word to find the vowels and consonants : ")
vowels=0
consonants=0
for letters in word:
    if letters.lower() in "aeiou" :
        vowels=vowels+1
    elif letters==" ":
        pass
    else:
        consonants= consonants+1
        
print("There are {} vowels in {}".format(vowels, word))
print("there are {} consonants in {}".format(consonants, word))