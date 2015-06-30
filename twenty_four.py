from itertools import *

def playTwentyFour():
    cards = raw_input('Enter a 4 digit number to represent 4 cards\n(or enter "q" to quit playing): ')
    while cards != 'q':
        cardValues = []
        for c in cards:
            if c == '0':
                cardValues.append('10')
            else:
                cardValues.append(c)
        print '\n---------------------------'
        print tfcombos(cardValues)
        print '---------------------------\n\n'
        cards = raw_input('Enter a 4 digit number to represent 4 cards\n(or enter "q" to quit playing): ')
    print "gg!"
    return None

def tfcombos(cardValues):
    for values in permutations(cardValues, 4):
        for operators in product('+-*/', repeat=3):
            if evalEquat(operators, values) == 24.0:
                return 'The combo is: ' + combEquat(operators, values)
    return 'No possible combination'

def combEquat(oprts, values):
    '''
    eg. ('*', '/', '+'), ('1', '3', '4', '10')
    returns '((1*3)/4)+10'
    '''
    return '(('+values[0]+oprts[0]+values[1]+')'+oprts[1]+values[2]+')'+oprts[2]+values[3]

def evalEquat(oprts, values):
    return eval('(('+'float(values[0])'+oprts[0]+values[1]+')'+oprts[1]+values[2]+')'+oprts[2]+values[3])

def isTwentyFour(cards):
    cardValues = []
    for c in cards:
        if c == '0':
            cardValues.append('10')
        else:
            cardValues.append(c)
    for values in permutations(cardValues, 4):
        for operators in product('+-*/', repeat=3):
            if evalEquat(operators, values) == 24.0:
                return True
    return False

def noSolutions():
    noSolutions = 0
    for combo in combinations_with_replacement('0123456789', 4):
        if not isTwentyFour(combo):
            noSolutions += 1
    return noSolutions

# total combo = 715, no solutions = 200

playTwentyFour()