import random
suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace')
values={'two': 2,'three': 3,'four': 4,'five': 5,'six': 6,'seven': 7,'eight': 8,'nine': 9,'ten': 10,'jack': 10,'queen': 10,'king': 10,'ace': 11}
playing=True
class card:
    def __init__(self,suits,ranks):
        self.suits=suits
        self.ranks=ranks
    def __str__(self):
        return f'{self.ranks} of {self.suits}'
class deck:
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(card(suit,rank))
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        single_card=self.deck.pop()
        return single_card
    def __str__(self) -> str:
        deck_comp=''
        for card in self.deck:
            deck_comp+=f'\n {card.__str__()}'
        return 'the deck has: '+ deck_comp
test=deck()
# print(test)
class hand:
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0
    def add_card(self,card):
        self.cards.append(card)
        self.value+=values[card.ranks]
    def adjust_for_ace(self):
        while self.value>21 and self.aces==0:
            self.value-=10
            self.aces-=1
# test_player=hand()
# test_player.add_card(test.deal())
# test_player.add_card(test.deal())
# print(test_player.value)
# for card1 in test_player.cards:
#     print(card1)
class chips:
    def __init__(self,total=100):
        self.total=total
        self.bet=0
    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet
def take(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('sorry, a bet must be an intiger!!! ')
        else:
            if chips.bet > chips.total :
                print('sorry, your bet can not exceed ',chips.total) 
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
def hit_or_stand(deck,hand):
    global playing
    while True :
        d=input('do you want to hit or stand (h/s)? ').lower()
        if d =='h' :
            print('OK !')
            hit(deck,hand)
        elif d=='s' :
            print('player stands. dealer is playing.')
            playing=False
        else :
            print('pleas anwser with h/s ')
            continue
        break
def show_some(player,dealer):
    print('\nDealer\'s Hand:')
    print(' <Card Hidden>')
    print('',dealer.cards[1])
    print('\nPlayer\'s Hand:',*player.cards,sep='\n ')
def show_all(player,dealer):
    print('\nDealer\'s Hand:',*dealer.cards,sep='\n ')
    print('Dealers\'s Hand =',dealer.value)
    print('\nPlayer\'s Hand:',*player.cards,sep='\n ')    
    print('Player\'s Hand =',player.value)
def player_busts(player,dealer,chips):
    print('Player busts!')
    chips.lose_bet()
def player_wins(player,dealer,chips):
    print('Player wins!')
    chips.win_bet()
def dealer_busts(player,dealer,chips):
    print('Dealer busts!')
    chips.win_bet()
def dealer_win(player,dealer,chips):
    print('Dealer wins!')
    chips.lose_bet()
def push(player,dealer,chips):
    print('Dealer and Player tie! It is a push.')

################################################################################################################################################################################################

while True:
    print('welcome to BlcakJack! get cloes to 21 as much as you can without gonig over!\nDealer hits untol she reaches 17. Aces count as 1 or 11. ')
    new_deck=deck()
    new_deck.shuffle()
    
    player_hand=hand()
    player_hand.add_card(new_deck.deal())
    player_hand.add_card(new_deck.deal())

    dealer_hand=hand()
    dealer_hand.add_card(new_deck.deal())
    dealer_hand.add_card(new_deck.deal())


    player_chips=chips()

    take(player_chips)

    while playing:
        hit_or_stand(new_deck,player_hand)

        show_some(player_hand,dealer_hand)

        if player_hand.value>21 :
            player_busts(player_hand,dealer_hand,player_chips)
            break

    if player_hand.value<=21:
        
        while dealer_hand.value>17:
            hit(new_deck,dealer_hand)
        
        show_all(player_hand,dealer_hand)

        if dealer_hand.value>21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value>player_hand.value:
            dealer_win(player_hand,dealer_hand,player_chips)    
        elif dealer_hand.value<player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
    
    print('\nplayer\'s winnings stand at',player_chips.total)
    
    while True :
        d=input('do you want to continue (y/n)? ').lower()
        if d =='y' :
            print('OK !')
            break
        elif d=='n' :
            print('BYE ! ')
            break
        else :
            print('pleas anwser with y/n ')
            continue
    if d=='n':
         break