'''
Created on Apr 3, 2022

@author: Joker
'''
import random
from _ast import arguments
class coin:
    def __init__(self,rare=False, clean=True, heads=True, **cash):
       
        for key,value in cash.items():
            setattr(self,key,value)
            
        self.heads=heads
        self.is_rare=rare
        self.is_clean=clean
        
        if self.is_rare:
            self.value=self.org_value*1.25
        else:
            self.value=self.org_value
        if self.is_clean:
            self.color= self.clean_color
        else:
            self.color=self.rusty_color
    
    def rust(self):
        self.color= self.rusty_color
    def clean(self):
        self.color=self.clean_color
    def __del__(self):
        print("Coin Spent!")
    def flip(self):
        head_op=[True,False]
        choice= random.choice(head_op)
        self.heads=choice
        
    def __str__(self):
        if self.org_value >=1:
            return "P{} coin".format(int(self.org_value))
        else:
            return "{}p coin".format(int(self.org_value *100))
        
class one_pence(coin):
    def __init__(self):
        data={
            "org_value":0.01,
            "clean_color": "bronze",
            "rusty_color": "brownish",
            "num_edges":1,
            "diameter":20.3,
            "thickness":1.52,
            "mass":3.56,
            }
        super().__init__(**data)
        
class two_pence(coin):
    def __init__(self):
        data={
            "org_value":0.02,
            "clean_color": "bronze",
            "rusty_color": "brownish",
            "num_edges":1,
            "diameter":25.9,
            "thickness":1.85,
            "mass":7.12,
            }
        super().__init__(**data)
        
class five_pence(coin):
    def __init__(self):
        data={
            "org_value":0.05,
            "clean_color": "silver",
            "rusty_color": None,
            "num_edges":1,
            "diameter":18.0,
            "thickness":1.77,
            "mass":3.25,
            }
        super().__init__(**data)
        
        def rust(self):
            self.color=self.clean_color
class ten_pence(coin):
    def __init__(self):
        data={
            "org_value":0.10,
            "clean_color": "silver",
            "rusty_color": None,
            "num_edges":1,
            "diameter":24.5,
            "thickness":1.85,
            "mass":6.50,
            }
        super().__init__(**data)
        
        def rust(self):
            self.color=self.clean_color
            
class twenty_pence(coin):
    def __init__(self):
        data={
            "org_value":0.20,
            "clean_color": "silver",
            "rusty_color": None,
            "num_edges":7,
            "diameter":21.4,
            "thickness":1.7,
            "mass":5.00,
            }
        super().__init__(**data)
        
        def rust(self):
            self.color=self.clean_color
            
class fifty_pence(coin):
    def __init__(self):
        data={
            "org_value":0.50,
            "clean_color": "silver",
            "rusty_color": None,
            "num_edges":7,
            "diameter":27.3,
            "thickness":1.78,
            "mass":8.00,
            }
        super().__init__(**data)
        
        def rust(self):
            self.color=self.clean_color
class Pound(coin):
    def __init__(self):
        data={
            "org_value":1.00,
            "clean_color": "gold",
            "rusty_color": "greenish",
            "num_edges":1,
            "diameter":22.5,
            "thickness":3.15,
            "mass":9.5,
            }
        super().__init__(**data)
    
    
class two_Pound(coin):
    def __init__(self):
        data={
            "org_value":2.00,
            "clean_color": "gold & silver",
            "rusty_color": "greenish",
            "num_edges":1,
            "diameter":28.4,
            "thickness":2.50,
            "mass":12.00,
            }
        super().__init__(**data)        
    

coins=[one_pence(),two_pence(), five_pence(), ten_pence(), twenty_pence(), fifty_pence(),Pound(), two_Pound()]

for coin in coins:
    arguments=[coin, coin.color, coin, coin.diameter, coin.thickness, coin.num_edges, coin.mass]
    
    string= "{}-color:{},value:{}, diameter(mm):{}, thickness(mm):{}, number of edges:{}, mass(g):{}".format(*arguments)
    
    print(string)