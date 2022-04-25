'''
Created on Apr 3, 2022

@author: Joker
'''
import random
class coin:
    def __init__(self,rare=False, clean=True):
        self.is_rare=rare
        self.is_clean=clean
        
class Pound:
    def __init__(self, rare=False):
        
        self.rare=rare
        
        if self.rare:
            self.value=1.25
        else:
            self.value=1.00
             
        
        self.color="gold"
        self.num_edges=1
        self.diameter=22.5#mm
        self.thickness=3.15#mm
        self.heads=True
    def __del__(self):
        print("Coin Spent!")
    def rust(self):
        self.color="greenish"
    def clean(self):
        self.color="gold"
    def flip(self):
        head_op=[True,False]
        choice= random.choice(head_op)
        self.heads=choice
        
    


coin1=Pound()
coin1.value
print(type(coin1))
print((coin1.value))
