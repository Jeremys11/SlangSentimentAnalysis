import pickle
from xlutils.copy import copy
from xlrd import *


fileWords2008Neg = open('2008Neg.pickle', 'rb')
fileWords2008Pos = open('2008Pos.pickle', 'rb')
fileWords2008Nt = open('2008Nt.pickle', 'rb')

fileWords2009Neg = open('2009Neg.pickle', 'rb')
fileWords2009Pos = open('2009Pos.pickle', 'rb')
fileWords2009Nt = open('2009Nt.pickle', 'rb')

fileWords2010Neg = open('2010Neg.pickle', 'rb')
fileWords2010Pos = open('2010Pos.pickle', 'rb')
fileWords2010Nt = open('2010Nt.pickle', 'rb')

fileCompareSlang = open("SlangSD.txt",encoding='utf8')

words2008Pos = pickle.load(fileWords2008Pos)
words2008Neg = pickle.load(fileWords2008Neg)
words2008Nt = pickle.load(fileWords2008Nt)

words2009Neg = pickle.load(fileWords2009Neg)
words2009Pos = pickle.load(fileWords2009Pos)
words2009Nt = pickle.load(fileWords2009Nt)

words2010Neg = pickle.load(fileWords2010Neg)
words2010Pos = pickle.load(fileWords2010Pos)
words2010Nt = pickle.load(fileWords2010Nt)


w = copy(open_workbook('Sentiments.xls'))

w.get_sheet(0).write(0,0,"Words")
w.get_sheet(0).write(0,1,"Positive")
w.get_sheet(0).write(0,2,"Negative")
w.get_sheet(0).write(0,3,"Neutral")
w.get_sheet(0).write(0,4,"Probability of Word")

w.get_sheet(0).write(0,6,"Positive")
w.get_sheet(0).write(0,7,"Negative")
w.get_sheet(0).write(0,8,"Neutral")
w.get_sheet(0).write(0,9,"Probability of Word")

w.get_sheet(0).write(0,11,"Positive")
w.get_sheet(0).write(0,12,"Negative")
w.get_sheet(0).write(0,13,"Neutral")
w.get_sheet(0).write(0,14,"Probability of Word")

w.get_sheet(0).write(0,16,"Total 2008 Positive")
w.get_sheet(0).write(0,17,"Total 2008 Negative")
w.get_sheet(0).write(0,18,"Total 2008 Neutral")

w.get_sheet(0).write(0,19,"Total 2009 Positive")
w.get_sheet(0).write(0,20,"Total 2009 Negative")
w.get_sheet(0).write(0,21,"Total 2009 Neutral")

w.get_sheet(0).write(0,22,"Total 2010 Positive")
w.get_sheet(0).write(0,23,"Total 2010 Negative")
w.get_sheet(0).write(0,24,"Total 2010 Neutral")

#################################################

w.get_sheet(0).write(0,26,"Word 2008 Positive")
w.get_sheet(0).write(0,27,"Word 2008 Negative")
w.get_sheet(0).write(0,28,"Word 2008 Neutral")

w.get_sheet(0).write(0,29,"Word 2009 Positive")
w.get_sheet(0).write(0,30,"Word 2009 Negative")
w.get_sheet(0).write(0,31,"Word 2009 Neutral")

w.get_sheet(0).write(0,32,"Word 2010 Positive")
w.get_sheet(0).write(0,33,"Word 2010 Negative")
w.get_sheet(0).write(0,34,"Word 2010 Neutral")

#################################################

w.get_sheet(0).write(0,36,"Word 2008 Sentiment")
w.get_sheet(0).write(0,37,"Word 2009 Sentiment")
w.get_sheet(0).write(0,38,"Word 2008 Sentiment")


total2008 = 0
total2009 = 0
total2010 = 0

pos2008 = 0
neg2008 = 0
nt2008 = 0

pos2009 = 0
neg2009 = 0
nt2009 = 0

pos2010 = 0
neg2010 = 0
nt2010 = 0

sentiments2008 = dict()
sentiments2009 = dict()
sentiments2010 = dict()
change08_09 = dict()
change08_10 = dict()
change09_10 = dict()

##
#Getting totals to calculate marginal probabilites
##
itr = 0
for word in words2008Neg:
    a = words2008Pos[word]
    b = words2008Neg[word]
    c = words2008Nt[word]

    d = words2009Pos[word]
    e = words2009Neg[word]
    f = words2009Nt[word]

    g = words2010Pos[word]
    h = words2010Neg[word]
    i = words2010Nt[word]

    total2008 += (a+b+c)
    total2009 += (d+e+f)
    total2010 += (g+h+i)

    pos2008 += a
    neg2008 += b
    nt2008 += c

    pos2009 += d
    neg2009 += e
    nt2009 += f

    pos2010 += g
    neg2010 += h
    nt2010 += i

    itr += 1

w.get_sheet(0).write(1,16,pos2008)
w.get_sheet(0).write(1,17,neg2008)
w.get_sheet(0).write(1,18,nt2008)

w.get_sheet(0).write(1,19,pos2009)
w.get_sheet(0).write(1,20,neg2009)
w.get_sheet(0).write(1,21,nt2009)

w.get_sheet(0).write(1,22,pos2010)
w.get_sheet(0).write(1,23,neg2010)
w.get_sheet(0).write(1,24,nt2010)

itr = 1
for word in words2008Neg:
    a = words2008Pos[word]
    b = words2008Neg[word]
    c = words2008Nt[word]

    w.get_sheet(0).write(itr, 0, word)
    w.get_sheet(0).write(itr, 1, a)
    w.get_sheet(0).write(itr, 2, b)
    w.get_sheet(0).write(itr, 3, c)
    w.get_sheet(0).write(itr, 4, (a+b+c) / total2008)
 
    #2009 
    d = words2009Pos[word]
    e = words2009Neg[word]
    f = words2009Nt[word]

    w.get_sheet(0).write(itr, 6, d)
    w.get_sheet(0).write(itr, 7, e)
    w.get_sheet(0).write(itr, 8, f)
    w.get_sheet(0).write(itr, 9, (d+e+f) / total2009)

    #2010
    g = words2010Pos[word]
    h = words2010Neg[word]
    i = words2010Nt[word]

    w.get_sheet(0).write(itr, 11, g)
    w.get_sheet(0).write(itr, 12, h)
    w.get_sheet(0).write(itr, 13, i)
    w.get_sheet(0).write(itr, 14, (g+h+i) / total2010)

    ####
    #Getting Naive Bayes Probabilities
    ###
    if(a+b+c > 0):
        naivePos2008 = ((words2008Pos[word]/pos2008) * (pos2008/total2008)) / ((a+b+c)/total2008)
        naiveNeg2008 = ((words2008Neg[word]/neg2008) * (neg2008/total2008)) / ((a+b+c)/total2008)
        naiveNt2008 = ((words2008Nt[word]/nt2008) * (nt2008/total2008)) / ((a+b+c)/total2008)
    else:
        naivePos2008 = 0
        naiveNeg2008 = 0
        naiveNt2008 = 0

    if (d+e+f > 0):
        naivePos2009 = ((words2009Pos[word]/pos2009) * (pos2009/total2009)) / ((d+e+f)/total2009)
        naiveNeg2009 = ((words2009Neg[word]/neg2009) * (neg2009/total2009)) / ((d+e+f)/total2009)
        naiveNt2009 = ((words2009Nt[word]/nt2009) * (nt2009/total2009)) / ((d+e+f)/total2009)
    else:
        naivePos2009 = 0
        naiveNeg2009 = 0
        naiveNt2009 = 0

    if (g+h+i > 0):
        naivePos2010 = ((words2010Pos[word]/pos2010) * (pos2010/total2010)) / ((g+h+i)/total2010)
        naiveNeg2010 = ((words2010Neg[word]/neg2010) * (neg2010/total2010)) / ((g+h+i)/total2010)
        naiveNt2010 = ((words2010Nt[word]/nt2010) * (nt2010/total2010)) / ((g+h+i)/total2010)
    else:
        naivePos2010 = 0
        naiveNeg2010 = 0
        naiveNt2010 = 0

    w.get_sheet(0).write(itr,26,naivePos2008)
    w.get_sheet(0).write(itr, 27, naiveNeg2008)
    w.get_sheet(0).write(itr, 28, naiveNt2008)

    w.get_sheet(0).write(itr, 29, naivePos2009)
    w.get_sheet(0).write(itr, 30, naiveNeg2009)
    w.get_sheet(0).write(itr, 31, naiveNt2009)

    w.get_sheet(0).write(itr, 32, naivePos2010)
    w.get_sheet(0).write(itr, 33, naiveNeg2010)
    w.get_sheet(0).write(itr, 34, naiveNt2010)


    ###
    #Assigning sentiments based on the most likely probability
    ###

    if naivePos2008 == max(naivePos2008,naiveNeg2008,naiveNt2008):
        w.get_sheet(0).write(itr, 36, 1)
        sentiments2008[word] = 1
    if naiveNeg2008 == max(naivePos2008,naiveNeg2008,naiveNt2008):
        w.get_sheet(0).write(itr, 36, -1)
        sentiments2008[word] = -1
    if naiveNt2008 == max(naivePos2008,naiveNeg2008,naiveNt2008):
        w.get_sheet(0).write(itr, 36, 0)
        sentiments2008[word] = 0

    ##########################################33
    if naivePos2009 == max(naivePos2009,naiveNeg2009,naiveNt2009):
        w.get_sheet(0).write(itr, 37, 1)
        sentiments2009[word] = 1
    if naiveNeg2009 == max(naivePos2009,naiveNeg2009,naiveNt2009):
        w.get_sheet(0).write(itr, 37, -1)
        sentiments2009[word] = -1
    if naiveNt2009 == max(naivePos2009,naiveNeg2009,naiveNt2009):
        w.get_sheet(0).write(itr, 37, 0)
        sentiments2009[word] = 0


    ##############################################33
    if naivePos2010 == max(naivePos2010,naiveNeg2010,naiveNt2010):
        w.get_sheet(0).write(itr, 38, 1)
        sentiments2010[word] = 1
    if naiveNeg2010 == max(naivePos2010,naiveNeg2010,naiveNt2010):
        w.get_sheet(0).write(itr, 38, -1)
        sentiments2010[word] = -1
    if naiveNt2010 == max(naivePos2010, naiveNeg2010, naiveNt2010):
        w.get_sheet(0).write(itr, 38, 0)
        sentiments2010[word] = 0

    ##
    #Measuring the change in sentiment over years
    ##
    change08_09[word] = sentiments2009[word] - sentiments2009[word]
    change08_10[word] = sentiments2010[word] - sentiments2008[word]
    change09_10[word] = sentiments2010[word] - sentiments2009[word]

    w.get_sheet(0).write(itr, 40, change08_09[word])
    w.get_sheet(0).write(itr, 41, change09_10[word])
    w.get_sheet(0).write(itr, 42, change08_10[word])

    itr += 1

pickling_on = open('sentiments2008.pickle', 'wb')
pickle.dump(sentiments2008, pickling_on)
pickling_on.close()

pickling_on = open('sentiments2009.pickle', 'wb')
pickle.dump(sentiments2009, pickling_on)
pickling_on.close()

pickling_on = open('sentiments2010.pickle', 'wb')
pickle.dump(sentiments2010, pickling_on)
pickling_on.close()

####################################################

pickling_on = open('change08_09.pickle', 'wb')
pickle.dump(change08_09, pickling_on)
pickling_on.close()

pickling_on = open('change08_10.pickle', 'wb')
pickle.dump(change08_10, pickling_on)
pickling_on.close()

pickling_on = open('change09_10.pickle', 'wb')
pickle.dump(change09_10, pickling_on)
pickling_on.close()


w.save('Sentiments.xls')