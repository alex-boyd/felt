#Poker hand logic and objects

#import

#constants
handNames =\
    [\
    "High Card",\
    "Pair",\
    "Two Pair",\
    "Three of a Kind",\
    "Straight",\
    "Flush",\
    "Full House",\
    "Straight Flush"\
    ]

suits = ["s","h","d","c"]

#class definitions

#card class stores name, value, and suit
class Card:
    def __init__(self, s, v, n):
        self.suit = s
        self.value = v
        self.name = n 
        self.boardImagePath = "cards/board/" + n + ".png"
        self.holeImagePath = "cards/hole/" + n + ".png"

    def getValue(self):
        return self.value

#hand class stores cards and value of best hand
class Hand:
    def __init__(self):
        self.handValue = 0
        self.highCardValue = 0
        self.secondCardValue = 0
        self.cardsInHand = []
        self.scoringCards = []
        self.kickers = []
        self.name = ''


#populate deck (optimize later?)
def getDeck():
    fullDeck = []

    for s in suits:
        for v in range(2,15):
            if v < 11:
                faceChar = str(v)
            if v == 11:
                faceChar = "J"
            if v == 12:
                faceChar = "Q"
            if v == 13:
                faceChar = "K"
            if v == 14:
                faceChar = "A"

            n = faceChar + s

            fullDeck.append(pu.Card(s, v, n)) 

    self.cached = True
    return fullDeck

#hands are ranked from 0 (high card) to 8 (straight flush)

#checks for pair (value 1) 
def Pair(hand):
    for cards in hand.cardsInHand:
        if instancesOf(hand, cards) == 2:
            hand.handValue = 1
            hand.highCardValue = cards.value
            for cards in hand.cardsInHand:
                if cards.value == hand.highCardValue:
                    hand.scoringCards.append(cards)
            return

#checks for two pair (value 2)
def TwoPair(hand):
    pairs = []
    for cards in hand.cardsInHand:
        if cards.value not in pairs:
            if (instancesOf(hand, cards)) == 2: 
                pairs.append(cards.value)
    if len(pairs) > 1:
        for pair in pairs:
            if pair > hand.highCardValue:
                hand.secondCardValue = hand.highCardValue
                hand.highCardValue = pair
            elif pair > hand.secondCardValue:
                hand.secondCardValue = pair


        for cards in hand.cardsInHand:
            if cards == hand.highCardValue or \
               cards.value == hand.secondCardValue:
                hand.scoringCards.append(cards)
        hand.handValue = 2


    return

#checks for three of a kind (value 3)
def ThreeOfAKind(hand):
    for cards in hand.cardsInHand:
        if instancesOf(hand, cards) == 3:
            hand.handValue = 3
            hand.highCardValue = cards.value
            for cards in hand.cardsInHand:
                if cards.value == hand.highCardValue:
                    hand.scoringCards.append(cards)
            return

#checks for straight (value 4)  
def Straight(hand):
    cardsInARow = 0
    highCard = 0
    straight = False
    sortedHand = hand.cardsInHand
    sortedHand.sort(key = lambda x: x.value)

    for id, card in enumerate(sortedHand):
        next = sortedHand[(id + 1) % len(sortedHand)]

        if \
        next.value - card.value == 1 or\
        id == len(sortedHand) - 1:
            hand.scoringCards.append(card)
            cardsInARow += 1

            if cardsInARow >= 5:
                straight = True
                highCard = card.value

        elif not straight: 
            cardsInARow = 0
            hand.handValue = 0
            hand.scoringCards = []

    if straight:
        #return highCard
        hand.highCardValue = highCard
        hand.handValue = 4

#check for flush (value 5)  
def Flush(hand):
    counts = {"c":0,"d":0,"h":0,"s":0}
    highCard = {"c":0,"d":0,"h":0,"s":0}
    suitedCards = {"c":[],"d":[],"h":[],"s":[]}
    for cards in hand.cardsInHand:
        counts[cards.suit] += 1 
        suitedCards[cards.suit].append(cards)
        if highCard[cards.suit] < cards.value:
            highCard[cards.suit] = cards.value
    for suit in counts:
        if counts[suit] >= 5:
            hand.scoringCards = suitedCards[suit]
            hand.highCardValue = highCard[suit]
            hand.handValue = 5
            return
    return 

#def FullHouse (value 6)
def FullHouse(hand):
    pairs = []
    sets = []
    for cards in hand.cardsInHand:
        if cards.value not in pairs:
            if (instancesOf(hand, cards)) == 2: 
                pairs.append(cards.value)
        if cards.value not in sets:
            if (instancesOf(hand,cards)) == 3:
                sets.append(cards.value)
    if len(pairs) > 0 and len(sets) > 0:
        for set in sets:
            if set > hand.highCardValue:
                hand.secondCardValue = hand.highCardValue
                hand.highCardValue = set
            elif set > hand.secondCardValue and set > hand.secondCardValue:
                hand.secondCardValue = set
            
        for pair in pairs:
            if pair > hand.secondCardValue:
                hand.secondCardValue = pair

        for cards in hand.cardsInHand:
            if cards.value == hand.secondCardValue or \
               cards.value == hand.highCardValue:
               hand.scoringCards.append(cards)


        hand.handValue = 6

#check for four of a kind (value 7)
def FourOfAKind(hand):
    for cards in hand.cardsInHand:
        if instancesOf(hand, cards) == 4:
            hand.handValue = 7
            hand.highCardValue = cards.value
            for cards in hand.cardsInHand:
                if cards.value == hand.highCardValue:
                    hand.scoringCards.append(cards)
 
    return

#check for straight flush (value 8)  
def StraightFlush(hand):
    Flush(hand)
    if(hand.handValue > 0):
        flush = Hand()
        flush.cardsInHand = hand.scoringCards
        Straight(flush)
        if(flush.handValue > 0):
            hand.handValue = 8

#helper functions?

#master function checks a hand for every hand type in descending order of value
def evaluateHand(hand):
    while True:
        StraightFlush(hand)
        if hand.handValue == 8:
            break
        FourOfAKind(hand)
        if hand.handValue == 7:
            break
        FullHouse(hand)
        if hand.handValue == 6:
            break
        Flush(hand)
        if hand.handValue == 5:
            break
        Straight(hand)
        if hand.handValue == 4:
            break
        ThreeOfAKind(hand)
        if hand.handValue == 3:
            break
        TwoPair(hand)
        if hand.handValue == 2:
            break
        Pair(hand)
        if hand.handValue == 1:
            break
        break
        
    hand.kickers = [c for c in hand.cardsInHand if c not in hand.scoringCards]
    hand.kickers.sort(key = lambda x: x.value)

#compares a hand that has been evaluated
#return -1 for left less than right, 0 for equal, 1 for left greater than right
def compareHands(left,right):
        if left.handValue < right.handValue:
            return -1

        if left.handValue > right.handValue:
            return 1

        if left.highCardValue < right.highCardValue:
            return -1

        if left.highCardValue > right.highCardValue:
            return 1

        if left.secondCardValue > 0:
            if left.secondCardValue < right.secondCardValue:
                return -1
            if left.secondCardValue > right.secondCardValue:
                return 1

        else:
            for s, o in zip(left.kickers,right.kickers):
                if s.value < o.value:
                    return -1
                if s.value > o.value:
                    return 1

        return 0

#counts instances of a card value
def instancesOf(hand, card):
    count = 0
    for cards in hand.cardsInHand:
        if cards.value == card.value:
            count += 1
    return count

