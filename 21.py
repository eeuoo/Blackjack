import random
from functools import reduce

deck = ['sa','s2','s3','s4','s5','s6','s7','s8','s9','s10','sj','sq','sk','ca','c2','c3','c4','c5','c6','c7','c8','c9','c10','cj','cq','ck','ha','h2','h3','h4','h5','h6','h7','h8','h9','h10','hj','hq','hk','da','d2','d3','d4','d5','d6','d7','d8','d9','d10','dj','dq','dk']

class Casting:
    def to_int(s):
        if type(s) == str:
            return int(s.strip())
        else:
            return s

class Card:
  
    def __init__(self):

        global deck
        self.cardlist = []                 
        self.numberlist = [] 

        random.shuffle(deck)
        self.card = deck.pop()
        self.cardlist.append(self.card)
        self.num = self.card.lstrip(self.card[0])
        
        if self.num == 'k' or self.num == 'q' or self.num == 'j':
            self.num = 10
        # elif 

        else : self.num = Casting.to_int(self.num)

        self.numberlist.append(self.num)

        # print(self.cardlist)
        # print(self.numberlist)
  

    def summation(self):

        self.cardsum = reduce(lambda x, y: x + y, self.numberlist)       
           


class Player(Card):
    def game(self):
        super().__init__()
        super().summation()
        
        print(self.cardlist)
    

        super().__init__()
        super().summation()
        if self.cardsum == 21:   print("승")

        elif self.cardsum > 21:   print("패")

        elif self.cardsum < 21:
            hitorstand = input("Hit 하고 싶으면 1, Stand 하고 싶으면 2를 입력하세요.")
            
            if hitorstand == '1':   
                self.num = self.card.lstrip(self.card[0])
                print("p cardsum>>" self.cardsum)
            

            if hitorstand == '2': 
                print("p cardsum>>" self.cardsum)

        

class Dealer(Card):
    def __init__(self):
        
        super().__init__()
        super().summation()

        print("d carsum>>" self.cardsum)

# a.cardlist()

a = Card()
a.summation()


b = Player()
b.game


a = Dealer()
