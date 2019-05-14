#import poker functions
import pokerUtilities as pu

def straightAndFlushTest():
    #test data
    sftest = [pu.Card("c",9,""),pu.Card("c",11,""),pu.Card("c",10,""),pu.Card("c",7,""),pu.Card("c",8,"")]
    stest = [pu.Card("s",9,""),pu.Card("c",11,""),pu.Card("c",10,""),pu.Card("c",7,""),pu.Card("c",8,"")]
    ftest = [pu.Card("c",9,""),pu.Card("c",11,""),pu.Card("c",10,""),pu.Card("c",7,""),pu.Card("c",8,"")]
    nosftest = [pu.Card("c",3,""),pu.Card("c",11,""),pu.Card("c",10,""),pu.Card("c",7,""),pu.Card("c",8,"")]
    nosftest2 = [pu.Card("s",9,""),pu.Card("c",11,""),pu.Card("c",10,""),pu.Card("c",7,""),pu.Card("c",8,"")]
    nostest = [pu.Card("s",3,""),pu.Card("c",11,""),pu.Card("c",10,""),pu.Card("c",7,""),pu.Card("c",8,"")]
    noftest = [pu.Card("d",9,""),pu.Card("c",11,""),pu.Card("c",10,""),pu.Card("c",7,""),pu.Card("c",8,"")]

    straightTest=pu.Hand()
    straightTest.cardsInHand = stest
    flushTest=pu.Hand()
    flushTest.cardsInHand = ftest
    straightFlushTest=pu.Hand()
    straightFlushTest.cardsInHand = sftest
    noStraightTest=pu.Hand()
    noStraightTest.cardsInHand = nostest
    noFlushTest=pu.Hand()
    noFlushTest.cardsInHand = noftest
    noStraightFlushTest=pu.Hand()
    noStraightFlushTest.cardsInHand = nosftest
    noStraightFlushTest2=pu.Hand()
    noStraightFlushTest2.cardsInHand = nosftest2

    print("\nregular straight:")
    pu.Straight(straightTest)
    print(straightTest.highCardValue)
    print(straightTest.handValue)
    print("\nregular flush:")
    pu.Flush(flushTest)
    print(flushTest.highCardValue)
    print(flushTest.handValue)
    print("\nstr8 flush:")
    pu.StraightFlush(straightFlushTest)
    print(straightFlushTest.highCardValue)
    print(straightFlushTest.handValue)
    print("\nno regular straight:")
    pu.Straight(straightTest)
    print(noStraightTest.highCardValue)
    print(noStraightTest.handValue)
    print("\nno regular flush:")
    pu.Flush(flushTest)
    print(noFlushTest.highCardValue)
    print(noFlushTest.handValue)
    print("\nno str8 flush no str8 :")
    pu.StraightFlush(straightFlushTest)
    print(noStraightFlushTest.highCardValue)
    print(noStraightFlushTest.handValue)
    print("\nno str8 flush (no flush):")
    pu.StraightFlush(noStraightFlushTest2)
    print(noStraightFlushTest2.highCardValue)
    print(noStraightFlushTest2.handValue)
        

def ofAKindTest(): 
    #test data
    test2 = [pu.Card("s",9,""),pu.Card("c",9,""),pu.Card("c",10,""),pu.Card("c",7,""),pu.Card("c",8,"")]
    test22 = [pu.Card("s",11,""),pu.Card("c",11,""),pu.Card("c",10,""),pu.Card("c",8,""),pu.Card("c",8,"")]
    test3 = [pu.Card("s",8,""),pu.Card("c",11,""),pu.Card("c",10,""),pu.Card("c",8,""),pu.Card("c",8,"")]
    test32 = [pu.Card("d",8,""),pu.Card("c",10,""),pu.Card("c",10,""),pu.Card("c",8,""),pu.Card("c",8,"")]
    test4 = [pu.Card("d",9,""),pu.Card("c",11,""),pu.Card("c",9,""),pu.Card("c",9,""),pu.Card("c",9,"")]
    testno2 = [pu.Card("s",3,""),pu.Card("c",9,""),pu.Card("c",10,""),pu.Card("c",7,""),pu.Card("c",8,"")]
    testno22 = [pu.Card("d",9,""),pu.Card("c",11,""),pu.Card("c",10,""),pu.Card("c",7,""),pu.Card("c",8,"")]
    testno3 = [pu.Card("d",9,""),pu.Card("c",11,""),pu.Card("c",10,""),pu.Card("c",7,""),pu.Card("c",8,"")]
    testno32 = [pu.Card("c",9,""),pu.Card("c",11,""),pu.Card("c",10,""),pu.Card("c",7,""),pu.Card("c",8,"")]
    testno4 = [pu.Card("c",9,""),pu.Card("c",11,""),pu.Card("c",10,""),pu.Card("c",7,""),pu.Card("c",8,"")]

    Pair=pu.Hand()
    Pair.cardsInHand = test2
    TwoPair=pu.Hand()
    TwoPair.cardsInHand = test22
    Set=pu.Hand()
    Set.cardsInHand = test3
    Boat=pu.Hand()
    Boat.cardsInHand = test32
    Four=pu.Hand()
    Four.cardsInHand = test4
    NoPair=pu.Hand()
    NoPair.cardsInHand = testno2
    NoTwoPair=pu.Hand()
    NoTwoPair.cardsInHand = testno22
    NoSet=pu.Hand()
    NoSet.cardsInHand = testno3
    NoBoat=pu.Hand()
    NoBoat.cardsInHand = testno32
    NoFour=pu.Hand()
    NoFour.cardsInHand = testno4

    print("\npair :")
    pu.Pair(Pair)
    print(Pair.highCardValue)
    print(Pair.secondCardValue)
    print(Pair.handValue)
    print("\ntwo pair:")
    pu.TwoPair(TwoPair)
    print(TwoPair.highCardValue)
    print(TwoPair.secondCardValue)
    print(TwoPair.handValue)
    print("\nset:")
    pu.ThreeOfAKind(Set)
    print(Set.highCardValue)
    print(Set.secondCardValue)
    print(Set.handValue)
    print("\nboat:")
    pu.FullHouse(Boat)
    print(Boat.highCardValue)
    print(Boat.secondCardValue)
    print(Boat.handValue)
    print("\nfour:")
    pu.FourOfAKind(Four)
    print(Four.highCardValue)
    print(Four.secondCardValue)
    print(Four.handValue)
    print("\nno pair :")
    pu.Pair(NoPair)
    print(NoPair.highCardValue)
    print(NoPair.secondCardValue)
    print(NoPair.handValue)
    print("\nno two pair:")
    pu.TwoPair(NoTwoPair)
    print(NoTwoPair.highCardValue)
    print(NoTwoPair.secondCardValue)
    print(NoTwoPair.handValue)
    print("\nno set:")
    pu.ThreeOfAKind(NoSet)
    print(NoSet.highCardValue)
    print(NoSet.secondCardValue)
    print(NoSet.handValue)
    print("\nno boat:")
    pu.FullHouse(NoBoat)
    print(NoBoat.highCardValue)
    print(NoBoat.secondCardValue)
    print(NoBoat.handValue)
    print("\nno four:")
    pu.FourOfAKind(NoFour)
    print(NoFour.highCardValue)
    print(NoFour.secondCardValue)
    print(NoFour.handValue)

def compareTest():
    sftest = [pu.Card("c",9,""),pu.Card("c",11,""),pu.Card("c",10,""),pu.Card("c",7,""),pu.Card("c",8,"")]
    stest = [pu.Card("s",9,""),pu.Card("c",11,""),pu.Card("c",10,""),pu.Card("c",7,""),pu.Card("c",8,"")]
    ftest = [pu.Card("c",3,""),pu.Card("c",11,""),pu.Card("c",10,""),pu.Card("c",7,""),pu.Card("c",8,"")]
    test2 = [pu.Card("s",9,""),pu.Card("c",9,""),pu.Card("c",10,""),pu.Card("c",7,""),pu.Card("c",8,"")]
    test22 = [pu.Card("s",11,""),pu.Card("c",11,""),pu.Card("c",10,""),pu.Card("c",8,""),pu.Card("c",8,"")]
    test3 = [pu.Card("s",8,""),pu.Card("c",11,""),pu.Card("c",10,""),pu.Card("c",8,""),pu.Card("c",8,"")]
    test32 = [pu.Card("d",8,""),pu.Card("c",10,""),pu.Card("c",10,""),pu.Card("c",8,""),pu.Card("c",8,"")]
    test4 = [pu.Card("d",9,""),pu.Card("c",11,""),pu.Card("c",9,""),pu.Card("c",9,""),pu.Card("c",9,"")]
    testk = [pu.Card("s",3,""),pu.Card("c",9,""),pu.Card("c",10,""),pu.Card("c",7,""),pu.Card("c",13,"")]

    hands = []

    Pair=pu.Hand()
    Pair.cardsInHand = test2
    Pair.name="Pair"
    hands.append(Pair)
    TwoPair=pu.Hand()
    TwoPair.cardsInHand = test22
    TwoPair.name="TwoPair"
    hands.append(TwoPair)
    Set=pu.Hand()
    Set.cardsInHand = test3
    Set.name="Set"
    hands.append(Set)
    Boat=pu.Hand()
    Boat.cardsInHand = test32
    Boat.name="Boat"
    hands.append(Boat)
    Four=pu.Hand()
    Four.cardsInHand = test4
    Four.name="Four"
    hands.append(Four)
    Kicker = pu.Hand()
    Kicker.cardsInHand = testk
    Kicker.name = "HighCard"
    hands.append(Kicker)
    straightTest=pu.Hand()
    straightTest.cardsInHand = stest
    straightTest.name ="straight"
    hands.append(straightTest)
    flushTest=pu.Hand()
    flushTest.cardsInHand = ftest
    flushTest.name = "flush"
    hands.append(flushTest)
    straightFlushTest=pu.Hand()
    straightFlushTest.cardsInHand = sftest
    straightFlushTest.name = "straightFlush"
    hands.append(straightFlushTest)

    for hand in hands:
        pu.evaluateHand(hand)
        print(hand.name + ": " + str(hand.handValue))

    for hand in hands:
        for other in hands:
            r = pu.compareHands(hand,other)
            m = ""
            if r == -1:
                m = " lost to " 
            elif r == 0:
                m = " tied with "
            elif r == 1:
                m = " dumpstered "
            s = hand.name + m + other.name
            print(s)




compareTest()
