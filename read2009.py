import json
import pickle

myfile0901 = open('RC_2009-01','r')

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

"""
And Now 2009

"""

itr = 0
#Getting sentences 0901
for line in myfile0901:
    print(itr)
    mylist.append(json.loads(line))
    temp = mylist[itr]['body'].split(' ')
    tempScore = mylist[itr]['score']
    for word in temp:
        if word.lower() in wordlist:
            if (tempScore == 0):
                wordlistNt[word.lower()] += 1
            elif (tempScore > 0):
                wordlistPos[word.lower()] += 1
            else:
                wordlistNeg[word.lower()] += 1
    itr += 1
    if(itr == 1000000):
        break

itr = 0
myfile0901.close()
mylist.clear()


pickling_on = open('2009Nt.pickle', 'wb')
pickle.dump(wordlistNt, pickling_on)
pickling_on.close()

pickling_on = open('2009Neg.pickle', 'wb')
pickle.dump(wordlistNeg, pickling_on)
pickling_on.close()

pickling_on = open('2009Pos.pickle', 'wb')
pickle.dump(wordlistPos, pickling_on)
pickling_on.close()