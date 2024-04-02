import random
class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        return (f"{self.rank["rank"]} of {self.suit}")

class Deck:
    def __init__(self):
        self.cards=[]
        suits =["spades","clubs","diamonds","hearts"]
        ranks =[
            {
                "rank":"2",
                "value":2
            },
            {
                "rank":"3",
                "value":3
            },
            {
                "rank":"4",
                "value":4
            },

            {
                "rank":"5",
                "value":5
            },
            {
                "rank":"6",
                "value":6
            },
            {
                "rank":"7",
                "value":7
            },
            {
                "rank":"8",
                "value":8
            },
            {
                "rank":"9",
                "value":9
            },
            {
                "rank":"10",
                "value":10
            },
            {
                "rank":"J",
                "value":10
            },
            {
                "rank":"Q",
                "value":10
            },
            {
                "rank":"K",
                "value":10
            },
            {
                "rank":"A",
                "value":11
            },
        ]

        for suit in suits:
            for rank in ranks:
                card = Card(rank,suit)
                self.cards.append(card)
    
    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)
        
    def deal(self,number):
        cards_deal=[]
        for i in range(number):
            if len(self.cards) > number:
                card = self.cards.pop()
                cards_deal.append(card)
        return cards_deal

class Hand:
    def __init__(self,dealer=False):
        self.cards = []
        self.value = 0  
        self.dealer = dealer

    def add_card(self,card_list):
        self.cards.extend(card_list)
    
    def calculator(self):
        has_ace = False
        self.value = 0  
        for card in self.cards:
            self.value += int(card.rank["value"])
            if card.rank["rank"] =="A":
                has_ace = True
        
        if has_ace and self.value > 21:
            self.value -=10
    
    def get_value(self):
        self.calculator()
        return self.value

    def is_blackjack(self):
        return self.get_value() == 21

    def display(self,show_dealer_cards=False):
        print(f'''{"Dealer's " if self.dealer else "Your "} hand :''')
        
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer and not show_dealer_cards and not self.is_blackjack():
                print("Hiden")
            else:
                print(card)

        if not self.dealer:
            print("Your value: ",self.get_value())

