import json
import pickle

myfile0801 = open('RC_2008-01','r')
myfile0802 = open('RC_2008-02','r')

wordlist = list()
wordlistNt = dict()
wordlistPos = dict()
wordlistNeg = dict()

slang = open("SlangSD.txt",encoding='utf8')
for line in slang:
    if(' ' not in line.split('\t')[0]):
        wordlist.append(line.split('\t')[0])
        wordlistNt[line.split('\t')[0]] = 0
        wordlistPos[line.split('\t')[0]] = 0
        wordlistNeg[line.split('\t')[0]] = 0

mylist = list()


#Getting sentences 0801
itr = 0
for line in myfile0801:
    print(itr)
    mylist.append(json.loads(line))
    temp = mylist[itr]['body'].split(' ')
    tempScore = mylist[itr]['score']
    for word in temp:
        if word.lower() in wordlist:
            if(tempScore == 0):
                wordlistNt[word.lower()] += 1
            elif(tempScore > 0):
                wordlistPos[word.lower()] += 1
            else:
                wordlistNeg[word.lower()] += 1
    itr += 1

itr = 0
mylist.clear()
myfile0801.close()


# Getting sentences 0802
for line in myfile0802:
    print(itr)
    mylist.append(json.loads(line))
    temp = mylist[itr]['body'].split(' ')
    tempScore = mylist[itr]['score']
    for word in temp:
        if word.lower() in wordlist:
            if(tempScore == 0):
                wordlistNt[word.lower()] += 1
            elif(tempScore > 0):
                wordlistPos[word.lower()] += 1
            else:
                wordlistNeg[word.lower()] += 1
    itr += 1

itr = 0
myfile0802.close()
mylist.clear()


pickling_on = open('2008Nt.pickle', 'wb')
pickle.dump(wordlistNt, pickling_on)
pickling_on.close()

pickling_on = open('2008Neg.pickle', 'wb')
pickle.dump(wordlistNeg, pickling_on)
pickling_on.close()

pickling_on = open('2008Pos.pickle', 'wb')
pickle.dump(wordlistPos, pickling_on)
pickling_on.close()

