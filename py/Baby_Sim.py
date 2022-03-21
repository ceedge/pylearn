'''
Created on Mar 20, 2022

@author: Joker
'''

from random import choice

questions=["Why is the sky blue?", 
           "Why is there a face on the moon?", 
           "Where are all the dinosaurs? "]
question=choice(questions)
anwser=input(question).lower()

while anwser != "just because":
    anwser= input("why? ").strip().lower()

print("Oh..Okay")
    