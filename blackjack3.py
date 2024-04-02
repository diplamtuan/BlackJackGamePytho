import random
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f'{self.rank["rank"]} of {self.suit}'

class Deck:
    def __init__(self):
        self.cards =[]
        suits=['spades','clubs','diamonds','hearts']
        ranks=[
            {
                'rank':"A",
                'value':11
            },
            {
                'rank':"2",
                'value':2
            },
            {
                'rank':"3",
                'value':3
            },
            {
                'rank':"4",
                'value':4
            },
            {
                'rank':"5",
                'value':5
            },
            {
                'rank':"6",
                'value':6
            },
            {
                'rank':"7",
                'value':7
            },
            {
                'rank':"8",
                'value':8
            },
            {
                'rank':"9",
                'value':9
            },
            {
                'rank':"10",
                'value':10
            },
            {
                'rank':"J",
                'value':10
            },
            {
                'rank':"Q",
                'value':10
            },
            {
                'rank':"K",
                'value':10
            },
        ]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit,rank))
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self,number):
        cards_deal = []
        for x in range(number):
            card = self.cards.pop()
            cards_deal.append(card)
        return cards_deal

class Hand:
    def __init__(self,dealer = False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self,card_list):
        self.cards.extend(card_list)

    def calculator_value(self):
        cards_value= 0
        has_ace = False
        for card in self.cards:
            if card.rank["rank"] == "A":
                has_ace = True
            card_value = card.rank["value"]
            cards_value += card_value          

        if has_ace and cards_value > 21:
            cards_value -= 10
        
        self.value = cards_value

    def get_value(self):
        self.calculator_value()
        return self.value

    def is_blackjack(self):
        self.calculator_value()
        if self.value == 21:
            return True
        return False
    def display(self,show_all_dealer_cards=False):
        print(f'''{"Dealer's hand" if self.dealer else "Your hand"} ''')
        for index,card in enumerate(self.cards):
            if index == 0 and self.dealer and not self.is_blackjack() and not show_all_dealer_cards:
                print("Hiden")
            else:
                print(card)

        if not self.dealer:
            print(f''' Value of {self.get_value()}''')

class Game:
    def play(self):
        game_number = 0
        game_to_play = 0

        while game_to_play <= 0:
            try:
                game_to_play = int(input("How many times do you want to play "))
            except:
                print("You must type a number")

        print()
        print("*" * 30)
        
        while game_number < game_to_play:
          
            game_number +=1
            print()
            print("*" * 30)
            print(f'''Game {game_number} of {game_to_play}''')
            print("*" * 30)
        
            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            player_hand.add_card(deck.deal(2))
            dealer_hand.add_card(deck.deal(2))

            player_hand.display()
            dealer_hand.display()

            if self.check__winner(player_hand, dealer_hand):
                continue

            choice = ""
            print()
            while player_hand.get_value() < 21 and choice not in ["s","stand"]:
                choice = input("Your choose 'hit' or 'stand' : ").lower()

                while choice not in ["s","stand","hit","h"]:
                    choice = input("Your choice 'hit' or 'stand' (H/S) ").lower()
                
                if choice in ["h","hit"]:
                    player_hand.add_card(deck.deal(1))
                    player_hand.display()
            if self.check__winner(player_hand, dealer_hand):
                continue

            while dealer_hand.get_value() < 17 and not dealer_hand.is_blackjack():
                dealer_hand.add_card(deck.deal(1))
                dealer_hand.get_value()

            dealer_hand.display(show_all_dealer_cards=True)
            if self.check__winner(player_hand, dealer_hand):
                continue
            print()
            player_hand.display()
            dealer_hand.display(show_all_dealer_cards=True)
            print()
            print("Your hand: ", player_hand.get_value())
            print("Dealer's hand: " , dealer_hand.get_value())
            self.check__winner(player_hand, dealer_hand,game_over=True)
        print("Thanks for playing...")    



    def check__winner(self,player_hand,dealer_hand, game_over=False):
        if not game_over:
            if player_hand.is_blackjack() and dealer_hand.is_blackjack():
                print ("You and dealer_hand blacjack ! Tie")
                return True
            elif player_hand.get_value() > 21:
                print("You are busted ! You lose")
                return True
            elif dealer_hand.get_value() > 21:
                print("dealer_hand is busted ! You win")
                return True
            elif player_hand.is_blackjack():
                print("You are blackjack ! You win")
                return True
            elif dealer_hand.is_blackjack():
                print("dealer_hand is blackack ! You lose")
                return True
        else:
            if player_hand.get_value() < dealer_hand.get_value():
                print("You lose")
                return True
            elif player_hand.get_value() > dealer_hand.get_value():
                print("You win")
                return True
            else:
                print("Tie!")
                return True
        return False

game = Game()
game.play()

        
# deck = Deck()
# deck.shuffle()

# player = Hand()
# dealer = Hand(dealer= True)

# player.add_card(deck.deal(2))
# dealer.add_card(deck.deal(2))

# player.display()
# dealer.display()