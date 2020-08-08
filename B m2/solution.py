# 
# Solution for "Digit Pairs"
#

from collections import Counter

'''
converts str list of list into int list of list

arg-1 : the list of str
returns : list of int
'''
def strList2IntList(theList):
    intDigitPairs = []
    for i in theList:
        intList = []
        for n in i:
            intList.append(int(n))
        intDigitPairs.append(intList)
    
    return intDigitPairs

'''
finds bit score pairs as per problem description

arg-1 : bit score list of int list of bit scores
returns number of pairs
'''
def findBitScorePairs(bitScoreList):
    evenList = []
    oddList = []
    for i in range(len(bitScoreList)):
        if(i%2 == 0):
            oddList.append(bitScoreList[i]) # odd as per 1 based index
        else:
            evenList.append(bitScoreList[i])

    MSBEven = convertMSBList(evenList)
    MSBOdd = convertMSBList(oddList)

    evenPairCount = findPairsCount(MSBEven)
    oddPairCount = findPairsCount(MSBOdd)

    return sum(evenPairCount + oddPairCount)

'''
arg-1 : list of items
returns : list of pairs for those items
'''
def findPairsCount(theList):
    theCountList = []

    c = Counter(theList)
    cList = list(c.items())

    for count in cList:
        theCountList.append(count[1] - 1)

    return theCountList

'''
arg-1 : the list of lits
returns : list of 1st items of every sub-list in the given list
'''
def convertMSBList(theList):
    MSBList = []
    for listItem in theList:
        MSBList.append(listItem[0])
    
    return MSBList


# static input
# N = 8
# digitPairs = [[2, 3, 4], [5, 6, 7], [3, 2, 1], [3, 4, 5], [1, 2, 3], [1, 1, 0], [7, 6, 7], [1, 1, 1]]

# User inputs
N = int(input('Enter number of "Digit pairs" :'))
digitPairs = [list(i) for i in input().split()]
digitPairs = strList2IntList(digitPairs) # converting into int


'''
finding bit score for number

arg-1 : number list of digit
returns : number list of bit score (last 2 digit)
'''
def findBitScore(numbList):
    theSum = (max(numbList) * 11) + (min(numbList) * 7)
    
    sumList = list(str(theSum))
    return [int(i) for i in sumList[-2:]]

bitScoreList = []
for numbList in digitPairs:
    bitScoreList.append(findBitScore(numbList))

print(findBitScorePairs(bitScoreList))
