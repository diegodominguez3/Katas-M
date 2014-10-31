def getValue(hand):
    value = ""
    if len(hand) < 5:
        return value
    
    #Full House
    last = 0
    last2 = ""
    cards = 1
    flsh = 1
    hand = sorted(hand, key=getsuit)
    hand2 = sorted(hand, key=getsuit2)
    con = ""
    con2 = ""
    n = 0
    for card in range(1,len(hand)+1):
        if hand[-card][0] == last:
            cards += 1
        else:
            cards = 1
        if cards == 3 and con2 != "3card":
            if n == hand[-card][0]:
                con2 = "3card"
            con = "3card"
            n = hand[-card][0]
        elif cards == 2 and con2 != "Pair" and n != hand[-card][0]:
            con = "Pair"
            n = hand[-card][0]
        if con != "":
            if (con == "Pair" and con2 == "3card") or (con == "3card" and con2 == "Pair"):
                return "Full House"
            con2 = con
            con = ""
        last = hand[-card][0]
    #Two Pair
    last = 0
    cards = 1
    condition = ""
    for card in range(1,len(hand)+1):
        if hand[-card][0] == last:
            cards += 1
        else:
            cards = 1
        if cards == 2 and con == "Pair":
            return "Two Pair"
        if cards == 2:
            con = "Pair"
        last = hand[-card][0]        
    #One Pair
    last = 0
    cards = 1
    for card in range(1,len(hand)+1):
        if hand[-card][0] == last:
            cards += 1
        else:
            cards = 1
        if cards == 2:
            return "One Pair"
        last = hand[-card][0]
def getsuit(card):
    return card[0]

def getsuit2(card):
    return card[1]

def tostring(hand):
    handtype = getValue(hand)
    strng = ""
    for card in hand:
        strng += (strhandval[card[0]]+card[1]) + " "
    strng = strng[:-1]
    if handtype != "":
        strng += (" " + handtype + "\n")
    else:
        strng += ("\n")
    return strng

def win(cards):
    cards = cards[:-1]
    if cards.find("Full House") != -1:
        pos = cards.find("Full House")
        return cards[0:pos+10] + " (winner)" + cards[pos+10::]
    elif cards.find("Flush") != -1:
        pos = cards.find("Flush")
        return cards[0:pos+5] + " (winner)" + cards[pos+5::]
    elif cards.find("Two Pair") != -1:
        pos = cards.find("Two Pair")
        return cards[0:pos+8] + " (winner)" + cards[pos+8::]
    elif cards.find("One Pair") != -1:
        pos = cards.find("One Pair")
        return cards[0:pos+8] + " (winner)" + cards[pos+8::]
    return cards
    
def order(game):
    r = ""
    for player in game:
        cards = []
        suits = []
        hand = []
        sub = []
        sub2 = []
        curnt = ""
        for card in player[::3]:
            cards.append(card)
        for suit in player[1::3]:
            suits.append(suit)
        for a,b in zip(cards,suits):
            hand.append(a+b)
        for item,suit in zip(hand,suits):
            sub = []
            sub.append(handval[item[0]])
            sub.append(suit)
            sub2.append(sub)
        curnt = tostring(sub2)
        r += curnt
    r = win(r)
    return r

def GetRankedGame(hands):
    game = hands.split("\n")
    return order(game)
    raise NotImplementedError

handval = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13, "A":14}
strhandval= {2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"T", 11:"J", 12:"Q", 13:"K", 14:"A"}

    
if __name__ == '__main__':
    print("Captura un mano por linea y una linea en blanco para terminar:")
    hands = ""
    line = input()
    while(line != ""):
        hands += line + "\n"
        line = input()
    print(GetRankedGame(hands))

