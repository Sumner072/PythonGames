# Mini-project #6 - Blackjack

import random

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

# initialize some useful global variables
in_play = False
outcome = ""
player_score = 0
dealer_score = 0
# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}


# global hand variables for players
# player_hand = []
# dealer_hand = []
# current_deck = []
# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print
            "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]],
                          CARD_SIZE)


# define hand class
class Hand:
    def __init__(self):
        self.cards_in_hand = []
        self.hand_value = 0
        # create Hand object

    def __str__(self):
        # return a string representation of a hand
        card_hand_string = "Your hand is "
        for card in range(len(self.cards_in_hand)):
            card_hand_string += str(self.cards_in_hand[card])
        return card_hand_string

    def add_card(self, card):
        self.cards_in_hand.append(card)  # add a card object to a hand
        return self.cards_in_hand

    def get_value(self):
        global VALUES
        self.hand_value = 0
        card_rank = ""
        # iterate through each card in hand to get rank and then value
        for card in self.cards_in_hand:
            # get rank
            card_rank = card.get_rank()
            # print "The card rank is " + str(card_rank)
            # get value
            self.hand_value += VALUES[card_rank]
            # print "The card value is " + str(VALUES[card_rank])
            # self.hand_value += card_value
            # begin logic for Aces being 11 if
        # for card in self.cards_in_hand:
        #    card_rank = card.get_rank()
        if card_rank != "A":
            return self.hand_value
        elif card_rank == "A" and self.hand_value + 10 <= 21:
            return self.hand_value + 10
        elif card_rank == "A" and self.hand_value + 10 > 21:
            return self.hand_value
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust

        # compute the value of the hand, see Blackjack video

    # Draw hand to canvas
    def draw(self, canvas, pos):
        for card in self.cards_in_hand:
            card.draw(canvas, [pos[0], pos[1]])
            pos[0] += CARD_SIZE[0]


# Hand Test
# test_hand = Hand()

# print test_hand
# print player_hand
# print dealer_hand

# define deck class
class Deck:
    def __init__(self):
        self.card_deck = []
        for suit in SUITS:
            for card_value in RANKS:
                self.card_deck.append(Card(suit, card_value))

    def shuffle(self):
        # shuffle the deck
        random.shuffle(self.card_deck)
        # use random.shuffle()
        return self.card_deck

    def deal_card(self):
        dealt_card = self.card_deck.pop()
        return dealt_card
        # print self.card_deck
        # deal a card object from the deck

    def __str__(self):
        card_deck_string = "Deck contains "
        for card in range(len(self.card_deck)):
            card_deck_string += (str(self.card_deck[card]) + " ")

        return str(card_deck_string)  # return a string representing the deck


# Deck Test
# test_deck = Deck()
# print test_deck
# for card in test_deck:
#    print card
# print type(test_deck)
# print len(test_deck.card_deck)
# test_deck.shuffle()
# print test_deck #shuffled_deck, works

# define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, dealer_hand, test_deck, dealer_score
    # shuffle test_deck
    test_deck = Deck()
    test_deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    # reset player hand and dealer hand
    player_hand.cards_in_hand = []
    dealer_hand.cards_in_hand = []
    player_hand.hand_value = 0
    dealer_hand.hand_value = 0
    # player_hand add initial 2 cards
    player_hand.add_card(test_deck.deal_card())
    player_hand.add_card(test_deck.deal_card())
    # for card in player_hand.cards_in_hand:
    # print "Player card: " + str(card)
    # dealer_hand add 2 initial cards
    dealer_hand.add_card(test_deck.deal_card())
    dealer_hand.add_card(test_deck.deal_card())
    # for card in dealer_hand.cards_in_hand:
    # print "Dealer card: " + str(card)
    # test the removal of cards from deck after dealt
    # print test_deck
    # print player_hand.get_value()
    # your code goes here
    if in_play:
        outcome = "You bailed, you lose."
        dealer_score += 1
        in_play = False
    else:
        in_play = True


def hit():
    global in_play, player_hand, dealer_hand, test_deck, outcome, dealer_score

    # if the hand is in play, hit the player
    if player_hand.get_value() <= 21 and in_play:
        # print "Before draw value:" + str(player_hand.get_value())
        player_hand.add_card(test_deck.deal_card())
        # print "After draw value:" + str(player_hand.get_value())
    # if busted, assign a message to outcome, update in_play and score
    if player_hand.get_value() > 21 and in_play:
        # print "You've busted."
        outcome = "You've busted."
        dealer_score += 1
        in_play = False


def stand():
    global in_play, player_hand, dealer_hand, test_deck, outcome, player_score, dealer_score
    if not in_play:
        # print "Game is over, stand does not work."
        pass
    else:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(test_deck.deal_card())
            # print "New dealer card hand value: " + str(dealer_hand.get_value())

    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play and dealer_hand.get_value() > 21:
        # print "Dealer busted, you won."
        outcome = "Dealer busted, you won."
        player_score += 1
        # print "Player hand value: " + str(player_hand.get_value())
        # print "Dealer hand value: " + str(dealer_hand.get_value())

    elif in_play and player_hand.get_value() <= dealer_hand.get_value():
        # print "You've lost, dealer had equal or higher score."
        outcome = "You've lost."
        dealer_score += 1
        # print "Player hand value: " + str(player_hand.get_value())
        # print "Dealer hand value: " + str(dealer_hand.get_value())

    elif in_play and player_hand.get_value() > dealer_hand.get_value():
        # print "You've won."
        outcome = "You've won."
        player_score += 1
        # print "Player hand value: " + str(player_hand.get_value())
        # print "Dealer hand value: " + str(dealer_hand.get_value())

    in_play = False
    # assign a message to outcome, update in_play and score


# draw handler
def draw(canvas):
    global player_hand, dealer_hand, in_play, player_score, dealer_score
    # test to make sure that card.draw works, replace with your code below

    # card = Card("S", "A")
    # card.draw(canvas, [300, 300]

    player_hand.draw(canvas, [100, 350])
    dealer_hand.draw(canvas, [100, 150])

    canvas.draw_text("Player Score: " + str(player_score), [100, 300], 30, "White")
    canvas.draw_text("Dealer Score: " + str(dealer_score), [100, 100], 30, "White")
    canvas.draw_text("Blackjack", [250, 50], 30, "Black")
    if in_play:
        # puts the card back over the dealer hole card since this draw function is called after the dealer draw function
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [100 + CARD_CENTER[0], 150 + CARD_CENTER[1]],
                          CARD_BACK_SIZE)
        canvas.draw_text("Hit or Stand?", [10, 550], 40, "Red")
    else:
        canvas.draw_text(outcome + "  New deal?", [10, 550], 40, "Red")


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

# create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit", hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()
