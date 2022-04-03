'''
Created on Mar 21, 2022

@author: Joker
'''
even_num= [x for x in range(1,1001) if x%2==0]

print(even_num)

odd_num=[x for x in range(1,1001) if x%2 != 0]
print(odd_num)

words= ["the", "quick", "jump", "over", "the", "lazy", "dog" ]
anwser= [[w.upper(), w.lower(), len(w)] for w in words]
print(anwser)