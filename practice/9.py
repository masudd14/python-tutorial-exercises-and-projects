import random
suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace')
values={'two': 2,'three': 3,'four': 4,'five': 5,'six': 6,'seven': 7,'eight': 8,'nine': 9,'ten': 10,'jack': 11,'queen': 12,'king': 13,'ace': 14}

class card:
    def __init__(self,suits,ranks):
        self.suits=suits
        self.ranks=ranks
        self.value=values[ranks]
    def __str__(self):
        return f'{self.ranks} of {self.suits}'
    
class deck:
    def __init__(self):
        self.all_card=[]
        for suit in suits:
            for rank in ranks:
                self.all_card.append(card(suit,rank))
    def shuffle(self):
        random.shuffle(self.all_card)
    def pick_card(self):
        return self.all_card.pop()

# my_deck=deck()
# print(my_deck.all_card[0])
# my_deck.shuffle()
# print(my_deck.pick_card())

class player:
    def __init__(self,name):
        self.name=name
        self.all_cards=[]
    def remove_one(self):
        return self.all_cards.pop(0)
    def add_cards(self,new_cards):
        if type(new_cards)== list:
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    def __str__(self) -> str:
        return f'player {self.name} has {len(self.all_cards)} cards'

player_one=player('one')
player_two=player('two')
new_deck=deck()
new_deck.shuffle()
ww=int(len(new_deck.all_card)/2)
for x in range (ww):
    player_one.add_cards(new_deck.pick_card())
    player_two.add_cards(new_deck.pick_card())
print(len(player_one.all_cards))
import pdb
game_on=True
round_num=0
while game_on:
    round_num+=1
    print(f'round {round_num}')
    if len(player_one.all_cards)==0 :
        print('player one got out of the cards , game over !!!')
        print('play two wins !!!')
        game_on=False
        break
    if len(player_two.all_cards)==0 :
        print('player two got out of the cards , game over !!!')
        print('play one wins !!!')
        game_on=False
        break
    play_one_cards=[]
    play_one_cards.append(player_one.remove_one())
    play_two_cards=[]
    play_two_cards.append(player_two.remove_one())
    while True:
        if play_one_cards[-1].value > play_two_cards[-1].value:
            player_one.add_cards(play_one_cards)
            player_one.add_cards(play_two_cards)
            break
        elif play_one_cards[-1].value < play_two_cards[-1].value:
            player_two.add_cards(play_one_cards)
            player_two.add_cards(play_two_cards)   
            break
        else:
            print('war goes on !!!')
            if len(player_one.all_cards) < 5:
                print('player one unable to play, game over !!!')
                print('player tow wins !!!')
                game_on=False
                break
            elif len(player_two.all_cards) < 5:
                print('player two unable to play, game over !!!')
                print('player one wins !!!')
                game_on=False
                break     
            else: 
                for num in range(5):
                    play_one_cards.append(player_one.remove_one())
                    play_two_cards.append(player_two.remove_one())