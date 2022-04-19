'''
Created on Apr 3, 2022

@author: Joker
'''


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
    def rust(self):
        self.color="greenish"
        
    


coin1=Pound()
coin1.value
print(type(coin1))
print((coin1.value))