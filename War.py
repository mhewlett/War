import random
print(
"""
 WW        WW     AAAAA     RRRRRRR
 WW   WW   WW   AA     AA   RR     RR
 WW  WWWW  WW   AAAAAAAAA   RRRRRRR 
 WW WW  WW WW   AA     AA   RR     RR
  WW  WW  WW    AA     AA   RR     RR
""")

print('Welcome to the game of War.\n'.center(40))

deck = ['AH','AD','AC','AS',
        '2H','2D','2C','2S',
        '3H','3D','3C','3S',
        '4H','4D','4C','4S',
        '5H','5D','5C','5S',
        '6H','6D','6C','6S',
        '7H','7D','7C','7S',
        '8H','8D','8C','8S',
        '9H','9D','9C','9S',
        '0H','0D','0C','0S',
        'JaH','JaD','JaC','JaS',
        'QH','QD','QC','QS',
        'KH','KD','KC','KS',
        'JoH','JoD','JoC','JoS']

def rename(card):
    num = ''
    suit = ''
    points = 0
    for x in card:
        for i in range(len(x)):
            if x[i] == 'a':
                num = 'Jack'
                points = 11
            if x[i] == 'o':
                num = 'Joker'
                points = 15
            if x[i] == 'A':
                num = 'Ace'
                points = 14
            if x[i] == '2':
                num = 'Two'
                points = 2
            if x[i] == '3':
                num = 'Three'
                points = 3
            if x[i] == '4':
                num = 'Four'
                points = 4
            if x[i] == '5':
                num = 'Five'
                points = 5
            if x[i] == '6':
                num = 'Six'
                points = 6
            if x[i] == '7':
                num = 'Seven'
                points = 7
            if x[i] == '8':
                num = 'Eight'
                points = 8
            if x[i] == '9':
                num = 'Nine'
                points = 9
            if x[i] == '0':
                num = 'Ten'
                points = 10
            if x[i] == 'Q':
                num = 'Queen'
                points = 12
            if x[i] == 'K':
                num = 'King'
                points = 13
            if x[i] == 'H':
                suit = 'Hearts'
            if x[i] == 'S':
                suit = 'Spades'
            if x[i] == 'C':
                suit = 'Clubs'
            if x[i] == 'D':
                suit = 'Diamonds'
    return num, suit, points

def computer(deck):
    computerDraw = random.randint(0, 55)
    card = deck[computerDraw]
    return card

def player(deck):
    playerDraw = random.randint(0, 55)
    card = deck[playerDraw]
    return card

def battle(cPoints,pPoints):
    Card = 1
    if pPoints > cPoints:
        input('***You won the battle!***'.center(40))
        return 1
    elif pPoints < cPoints:
        input('***You lost the battle!***'.center(40))
        return 2
    else:
        print('Your card value\'s are tied'.center(40))
        input('THIS MEANS WAR!'.center(40))
        return 3


def war(cCard, pCard, cDeck, pDeck, burn):
    c = []
    p = []
    temp = ''
    v, s, cb = rename(cCard)
    temp = v + ' of ' + s
    c.append(temp)
    v, s, pb = rename(pCard)
    temp = v + ' of ' + s
    p.append(temp)
    for y in range(4):
        temp = (player(deck))
        if temp not in burn:
            burn.append(temp)
        else:
            while temp in burn:
                temp = player(deck)
        v, s, pb = rename(temp)
        temp = v + ' of ' + s
        p.append(temp)

    for x in range(4):
        temp = (computer(deck))
        if temp not in burn:
            burn.append(temp)
        else:
            while temp in burn:
                temp = computer(deck)
        v, s, cb = rename(temp)
        temp = v + ' of ' + s
        c.append(temp)
    input('You and the enemy place '
          'three cards face down.\n')
    input('You both draw a card to '
          'to determine the war.\n')
    pPlay = p[-1]
    cPlay = c[-1]
    input('You play'.ljust(21,'.') + pPlay)
    print('The enemy plays'.ljust(21,'.') + cPlay)
    print()
    res = battle(cb,pb)
    if res == 1:
        return 1, p, c
    elif res == 2:
        return 2, p, c
    elif res == 3:

        war(cCard, pCard, cDeck, pDeck, burn)

loop = 'y'

while loop.lower() == 'y':

    burn = []
    computerDeck = 28
    playerDeck = 28
    battleCount = 0
    while computerDeck != 0 or playerDeck != 0:
        if len(burn) == 55:
            burn = []
        battleCount += 1
        computerDeck -= 1
        playerDeck -= 1
        card = 0
        computerCard = (computer(deck))
        if computerCard in burn:
            while computerCard in burn:
                computerCard = computer(deck)
        burn.append(computerCard)
        cValue, cSuit, cPoint = rename(computerCard)
        playerCard = (player(deck))
        if playerCard in burn or playerCard == computerCard:
            while playerCard in burn:
                playerCard = player(deck)
        burn.append(playerCard)
        pValue, pSuit, pPoint = rename(playerCard)

        print('  Battle: '.rjust(23) + str(battleCount))

        input('Ready to battle?'.center(38))
        input('Press enter to draw your card.'.center(40))
        print()
        print(''.center(40,'*'))
        print()
        input('You play'.ljust(21,'.') + pValue + ' of ' + pSuit)
        print('The enemy plays'.ljust(21, '.') + cValue + ' of ' + cSuit)
        print()
        results = battle(cPoint,pPoint)
        print(''.center(40, '-'))
        if results == 1:
            playerDeck += 2
            print('You keep your card and take theirs.'.center(40))
            print('      You have ' + str(playerDeck) + ' cards remaining.')
            print('   The enemy has ' + str(computerDeck) + ' cards remaining.')
        elif results == 2:
            computerDeck += 2
            print('You have lost one card from your deck.'.center(40))
            print('      You have ' + str(playerDeck) + ' cards remaining.')
            print('   The enemy has ' + str(computerDeck) + ' cards remaining.')
        elif results == 3:
            r, pHand, cHand = war(computerCard, playerCard, computerDeck, playerDeck, burn)
            pNum = len(pHand)
            cNum = len(cHand)
            if r == 1:
                playerDeck += cNum
                computerDeck -= cNum
                for x in cHand:
                    if x in burn:
                        burn.remove(x)
                pHand = []
                print('*****You won the war!*****'.center(40))
                print('You keep your cards and take all ' + str(cNum) + ' of theirs.')
                print('      You have ' + str(playerDeck) + ' cards remaining.')
                print('   The enemy has ' + str(computerDeck) + ' cards remaining.')
            elif r == 2:
                computerDeck += pNum
                playerDeck -= pNum
                for x in pHand:
                    if x in burn:
                        burn.remove(x)
                cHand = []
                print('*****You lost the war!*****'.center(40))
                print('            You lose ' + str(pNum) + ' cards.')
                print('      You have ' + str(playerDeck) + ' cards remaining.')
                print('   The enemy has ' + str(computerDeck) + ' cards remaining.')
            #elif r == 3:
                #r, pHand, cHand = war(computerDeck, playerDeck)
        print(''.center(40, '-'))
        input(''.center(40, '*'))
        print()
        if computerDeck == 0:
            print('Enemy is out of cards.\n'
                  'You win!')
            break
        elif playerDeck == 0:
            print('You are out of cards.\n'
                  'You lose.')
            break
    print('Do you wish to declare another war? (y)es or (n)o:')
    loop = input('> ')



