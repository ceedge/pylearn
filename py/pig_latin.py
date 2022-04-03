'''
Created on Mar 21, 2022

@author: Joker
'''
# get sentence from user
## split sentence into words
# loop through words and convert to pig latin
#stick words back together
# out put the final string
#from for_loop import vowels
#from comprehension import words

original= input("please make a sentence to convert to pig latin: ").lower().strip()
word= original.split()
print(word)

new_word=[]

for words in word:
    if words[0] in "aeiou":
        new_words=words+"yay"
        new_word.append(new_words)
   
    else:
        vowel_pos=0
        for letter in words:
            if letter not in "aeiou":
                vowel_pos= vowel_pos +1
            else:
                break
        con=words[:vowel_pos]
        the_rest= words[vowel_pos:]
        new_words= the_rest+con+"ay"
        new_word.append(new_words)


print(new_word)

op=" ".join(new_word)
print(op)