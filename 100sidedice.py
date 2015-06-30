from random import *
import pylab as pl

def throwuntil(n):
    init = 0
    result = randrange(1, 101)
    while result < n:
        init -= 1
        result = randrange(1, 101)
    return init + result

def trial(n, t=1000):
    loTrials = []
    for trial in range(t):
        loTrials.append(throwuntil(n))
    mean = sum(loTrials)/float(t)
    return mean

def allProfit(numoTrials=5000):
    profit = []
    for goal in range(1, 101):
        profit.append(trial(goal, numoTrials))
    return profit

AP = allProfit()

# profit = optGoal(AP)
pl.plot(AP)
pl.axis([0, 100, 0, 100])
pl.show()

