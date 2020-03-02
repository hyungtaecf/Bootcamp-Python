#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)


######## My notes ########

# Step 1:
# DONE # shuffle the cards
# DONE # give 26 cards to each player faced down and do not look at them

# Step 2:
# DONE # Flip the top cards of the deck at the same time
# DONE # The card with the higher value wins (A is the highest and 2 is the lowest)
# DONE # The winner takes both cards
# DONE # Place them face up at the bottom of their pile

# Step 3:
# Continue flipping
# DONE # When you reach the cards that are faced up, shuffle the cards and start at the top

# Step 4:
# DONE # If you flip two cards of equal value, war begins
# DONE # Both players take a card from the top of their pile and set it face down on top of the first card
# DONE # (some variants have three face down cards)
# DONE # Then take a third card and flip it face up
# DONE # The player whose up card has the higher value wins all six cards

# Step 5:
# DONE # If the two cards are also a tie, war is declared again and the process repeats until a player has a higher value
# First player to capture all the 52 of the cards wins

# Bonus:
# Implement some choice: the order of the cards when they return to the deck

from random import shuffle
from os import system, name

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self, suites, ranks):
        self.cards = []
        for suite in suites:
            for rank in ranks:
                self.cards.append(Card(suite, rank))

    def split_in_half(self):
        first_half = []
        second_half = []
        while len(self.cards)>0:
            first_half.append(self.cards.pop(0))
            second_half.append(self.cards.pop(0))
        return (first_half, second_half)

    def shuffle_cards(self):
        shuffle(self.cards)

    def __len__():
        return len(self.cards)

    def __str__(self):
        string = ""
        for card in self.cards:
            string+=str(card)+"\n"
        return string

class Hand(Deck):
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, cards):
        self.cards = cards

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self):
        if len(self.cards)>0:
            return self.cards.pop(0)
        else:
            return None


class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
        pass

    def take_cards(self, table):
        temp = Hand([])
        while len(table.cards)>0:
            temp.add_card(table.cards.pop(0))
        self.face_cards_up(temp)
        # TODO: BONUS -> function to reordenate the cards before take'em
        while len(temp.cards)>0:
            self.hand.add_card(temp.cards.pop(0))

    def face_cards_down(self, object):
        for card in object.cards:
            card.face_down()

    def face_cards_up(self, object):
        for card in object.cards:
            card.face_up()

    def play_card(self, table):
        card = self.hand.remove_card()
        if card != None:
            card.face_up()
            table.add_card(card)
            table.set_card(self, card)
            return True
        else:
            return False

    def play_3_cards_down(self, table):
        number_of_cards = 0
        while number_of_cards < 3 and self.have_cards():
            card = self.hand.remove_card()
            card.face_down()
            table.add_card(card)
            number_of_cards+=1
        return number_of_cards

    def have_cards(self):
        return len(self.hand.cards)>0

    def check_next_card_faced_up(self):
        return self.hand.cards[0].faced_up

    def shuffle_cards_down(self):
        self.face_cards_down(self.hand)
        self.hand.shuffle_cards()

    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.hand)

class Card:
    """
    Card class. It represents one card from a deck.
    It has attributes of rank, suite, and a boolean to know if it's faced up or down.
    """
    def __init__(self, suite, rank):
        self.suite = suite
        self.rank = rank
        self.faced_up = False

    def face_up(self):
        self.faced_up = True;

    def face_down(self):
        self.faced_up = False;

    def get_rank(self):
        count = 0
        for rank in RANKS:
            if self.rank == rank:
                break
            else:
                count += 1
        return count

    def __str__(self):
        if(self.faced_up):
            if len(self.rank) == 2:
                return "[ {r} {s} ]".format(r=self.rank,s=self.suite)
            else:
                return "[ {r}  {s} ]".format(r=self.rank,s=self.suite)
        else:
            return "[ DOWN ]"

class Table(Deck):
    def __init__(self, player, opponent):
        self.cards=[]
        self.player = player
        self.opponent = opponent
        self.player_card = Card(" "," ")
        self.opponent_card = Card(" "," ")

    def set_card(self, player, card):
        if(player == self.player):
            self.player_card = card
        else:
            self.opponent_card = card

    def add_card(self, card):
        self.cards.append(card)

    def compare_cards(self):
        if self.player_card.get_rank()>self.opponent_card.get_rank():
            return "player"
        elif self.player_card.get_rank()<self.opponent_card.get_rank():
            return "opponent"
        else:
            return "war"

    def __str__(self):
        string = Deck.__str__(self)+"\n\n\n"
        if len(self.cards)>0:
            string += str(self.player) + "'s current card: " + str(self.player_card)
            string += "\n"+ str(self.opponent) + "'s current card: " + str(self.opponent_card)
        return string

class Game():
    def __init__(self, table):
        self.player = table.player
        self.opponent = table.opponent
        self.table = table
        self.over = False
        self.war = False
        self.log = ""

    def game_over(self, winner):
        self.log += "{} WINS!!".format(str(winner))+"\n"
        self.over = True

    def check_cards(self):
        if not self.player.have_cards():
            self.game_over(self.opponent)
            return False
        elif not self.opponent.have_cards():
            self.game_over(self.player)
            return False
        else:
            self.check_next_card(self.player)
            self.check_next_card(self.opponent)
            return True

    def check_next_card(self, player):
        if player.check_next_card_faced_up():
            self.log+="{}'s next card is faced up.".format(player)+"\n"
            player.shuffle_cards_down()
            self.log+="*{} face cards down and shuffle them*".format(player)+"\n"

    def battle(self):
        if self.player.play_card(table) and self.opponent.play_card(table):
            print(game)
            self.log+="*Players play the cards*"+"\n"
            next()
            if self.table.compare_cards() == "player":# TODO: Simplify code returning the player itself instead
                self.player.take_cards(table)
                if self.war:
                    self.log+="{} wins the war and takes all the cards!\n".format(str(self.player))+"\n"
                    self.war=False
                else:
                    self.log+="{} wins the battle and takes the cards!\n".format(str(self.player))+"\n"
            elif table.compare_cards() == "opponent":
                self.opponent.take_cards(table)
                if self.war:
                    self.log+="{} wins the war and takes all the cards!\n".format(str(self.opponent))+"\n"
                    self.war=False
                else:
                    self.log+="{} wins the battle and takes the cards!\n".format(str(self.opponent))+"\n"
            else:
                self.log+="PREPARE YOURSELVES, BECAUSE IT IS A WAR!!!"+"\n"
                self.war=True
                if self.player.play_3_cards_down(self.table) < 3 or not self.player.have_cards:
                    self.log+="{} doesn't have enough cards to play!".format(str(self.player))+"\n"
                    self.game_over(opponent)
                elif self.opponent.play_3_cards_down(self.table) < 3 or not self.opponent.have_cards:
                    self.log+="{} doesn't have enough cards to play!".format(str(self.opponent))+"\n"
                    self.game_over(player)
                else:
                    self.battle()

    def release_log(self):
        temp=self.log
        self.log = ""
        return temp

    def __str__(self):
        string= "{}'s hand: {}\n".format(str(player),len(player.hand.cards))
        for card in range(len(player.hand.cards)):
            string+="|"
        string+= "\n\n{}'s hand: {}\n".format(str(opponent),len(opponent.hand.cards))
        for card in range(len(opponent.hand.cards)):
            string+="|"
        string+= "\n\n"+str(table)+"\n\n"
        string+= self.release_log()
        return string

def next():
    cmd = input("\nPress Enter to continue...")
    # for windows
    if name == 'nt':
        system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        system('clear')
    if cmd == "end":
        return True

######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Use the 3 classes along with some logic to play a game of war!

# Initialization
next()
player_name = input("What is your name? ")
opponent_name = input("What is your opponent's name? ")
deck = Deck(SUITE, RANKS)
print("\nOkay. So, here is the deck!")
next()
print("*Suffling the deck*\n")
deck.shuffle_cards()
print("The deck was shuffled.")
print("*Splitting the deck*")
splitted_deck = deck.split_in_half()
print("The deck was splitted in half.")
player_hand = Hand(splitted_deck[0])
print("\n{}, take your half.".format(player_name))
print("*Taken*")
opponent_hand = Hand(splitted_deck[1])
print("{} takes their half.".format(opponent_name))


player = Player(player_name, player_hand)
opponent = Player(opponent_name, opponent_hand)
table = Table(player, opponent)
game = Game(table)
next()
print(game)
next()

# Game Starts
while game.over == False:
    if game.check_cards():
        game.battle()
    print(game)
    if next():
        break
