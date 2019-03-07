import pickle
import matplotlib.pyplot as plt

"""
fileWords2008Neg = open('2008Neg.pickle', 'rb')
fileWords2008Pos = open('2008Pos.pickle', 'rb')
fileWords2008Nt = open('2008Nt.pickle', 'rb')

fileWords2009Neg = open('2009Neg.pickle', 'rb')
fileWords2009Pos = open('2009Pos.pickle', 'rb')
fileWords2009Nt = open('2009Nt.pickle', 'rb')

fileWords2010Neg = open('2010Neg.pickle', 'rb')
fileWords2010Pos = open('2010Pos.pickle', 'rb')
fileWords2010Nt = open('2010Nt.pickle', 'rb')

words2008Pos = pickle.load(fileWords2008Pos)
words2008Neg = pickle.load(fileWords2008Neg)
words2008Nt = pickle.load(fileWords2008Nt)

words2009Neg = pickle.load(fileWords2009Neg)
words2009Pos = pickle.load(fileWords2009Pos)
words2009Nt = pickle.load(fileWords2009Nt)

words2010Neg = pickle.load(fileWords2010Neg)
words2010Pos = pickle.load(fileWords2010Pos)
words2010Nt = pickle.load(fileWords2010Nt)
"""

fileSentiments2008 = open('sentiments2008.pickle', 'rb')
fileSentiments2009 = open('sentiments2009.pickle', 'rb')
fileSentiments2010 = open('sentiments2010.pickle', 'rb')

sentiments2008 = pickle.load(fileSentiments2008)
sentiments2009 = pickle.load(fileSentiments2009)
sentiments2010 = pickle.load(fileSentiments2010)

slang = dict()
fileCompareSlang = open("SlangSD.txt",encoding='utf8')
for line in fileCompareSlang:
    if(' ' not in line.split('\t')[0]):
        slang[line.split('\t')[0]] = int(line.split('\t')[1])

######################################################

counter08_09 = 0
counter09_10 = 0
counter08_10 = 0
size = len(sentiments2008)
for word in sentiments2008:
    if(sentiments2009[word] < 0 and sentiments2008[word] < 0):
        counter08_09 += 1
    elif(sentiments2009[word] >= 1 and sentiments2008[word] >= 1):
        counter08_09 += 1
    elif(sentiments2009[word] == 0 and sentiments2008[word] == 0):
        counter08_09 += 1
    else:
        counter08_09 += 0

    if(sentiments2010[word] < 0 and sentiments2009[word] < 0):
        counter09_10 += 1
    elif(sentiments2010[word] >= 1 and sentiments2009[word] >= 1):
        counter09_10 += 1
    elif(sentiments2010[word] == 0 and sentiments2009[word] == 0):
        counter09_10 += 1
    else:
        counter09_10 += 0

    if(sentiments2008[word] < 0 and sentiments2010[word] < 0):
        counter08_10 += 1
    elif(sentiments2008[word] >= 1 and sentiments2010[word] >= 1):
        counter08_10 += 1
    elif(sentiments2008[word] == 0 and sentiments2010[word] == 0):
        counter08_10 += 1
    else:
        counter08_10 += 0

print("Change 2008 to 2009: ", counter08_09/size)
print("Change 2009 to 2010: ", counter09_10/size)
print("Change 2008 to 2010: ", counter08_10/size)


####################################################

counter2008 = 0
counter2009 = 0
counter2010 = 0
size = len(slang)
for word in slang:
    if(slang[word] < 0 and sentiments2008[word] < 0):
        counter2008 += 1
    elif(slang[word] >= 1 and sentiments2008[word] >= 1):
        counter2008 += 1
    elif(slang[word] == 0 and sentiments2008[word] == 0):
        counter2008 += 1
    else:
        counter2008 += 0

    if(slang[word] < 0 and sentiments2009[word] < 0):
        counter2009 += 1
    elif(slang[word] >= 1 and sentiments2009[word] >= 1):
        counter2009 += 1
    elif(slang[word] == 0 and sentiments2009[word] == 0):
        counter2009 += 1
    else:
        counter2008 += 0

    if(slang[word] < 0 and sentiments2010[word] < 0):
        counter2010 += 1
    elif(slang[word] >= 1 and sentiments2010[word] >= 1):
        counter2010 += 1
    elif(slang[word] == 0 and sentiments2010[word] == 0):
        counter2010 += 1
    else:
        counter2010 += 0

print("Comparison 2008 to Slang: ",counter2008/size)
print("Comparison 2009 to Slang: ",counter2009/size)
print("Comparison 2010 to Slang: ",counter2010/size)

#############################################################
counter2010Pos = 0
counter2010Neg = 0
counter2010Nt = 0

for word in sentiments2010:
    if sentiments2010[word] > 0:
        counter2010Pos += 1
    if sentiments2010[word] < 0:
        counter2010Neg += 1
    if  sentiments2010[word] == 0:
        counter2010Nt += 1

print(counter2010Pos)
print(counter2010Neg)
print(counter2010Nt)