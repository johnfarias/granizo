# -*- coding: utf-8 -*-
"""
This function describe a serie of 3x+1, or siracusa problem.

f(x) = {3*x+1 if x is odd; x/2 if pair}
"""
from math import *
from matplotlib import pyplot as plt
from numpy import array, logical_not, sort, vectorize
from pandas import DataFrame

def f(x):
    s = [x]
    if x==1:
        return s
    else:            
        if x%2==0:
            return s + f(x//2)
        else:
            return s + f(3*x+1)

def serie(n):
    return [f(x) for x in range(2,n)]

def isDiv2(x):
    if x%2==0:
        return True
    else:
        return False
    
def isDiv4(x):
    if x%4==0:
        return True
    else:
        return False
    
def isNextPair(x):
    isPair = False
    nextPair = False
    if isDiv2(x):
        isPair = True
    if isDiv4(x):
        nextPair = True
    if isPair and nextPair:
        return True
    elif isPair and not nextPair:
        return False
    elif not isPair:
        return True
    
def powerOf2(x):
    if isDiv2(x):
        p = log(x)/log(2)
        if (p-floor(p))==0:
            return p
        else:
            return -1
    else:
        return -1
        
def plotRange(x):
    #data = {}
    for i in range(2,x):
        #data[i] = f(i)
        #plt.plot(data)
        plt.plot(f(i))
    plt.show()
    
def plotOnly(x):
    plt.plot(f(x))
    plt.show()
    
def studyOnly(x):
    s = array(f(x))
    l = len(s)
    mx = max(s)
    imx = list(s).index(mx)
    isPair = vectorize(isDiv2)
    p = sort(s[isPair(s)])
    i = sort(s[logical_not(isPair(s))])
    numPairs = len(p)
    numOdds = len(i)
    
    data = {
        'n':x,
        'serie':s,
        'sortSerie':sort(s),
        'length':l,
        'max':mx,
        'indexOfMax':imx,
        'pairs':p,
        'odd':i,
        'numPairs':numPairs,
        'numOdds':numOdds
        }
    return data

def studyRange(x):
    data = DataFrame(columns=['n','serie','sortSerie','length','max','indexOfMax','pairs','odd','numPairs','numOdds'])
    for i in range(2,x):
        data.loc[i] = studyOnly(i)
    data.to_csv('syracusa.csv',index=False)
    return data