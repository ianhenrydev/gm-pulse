import csv, string

def modScores(scores, controversial):
    if (controversial):
        scores[0] = int(scores[0]) + 1
    else:
        scores[1] = int(scores[1]) + 1
    return scores

def getFeatures(filename):
    with open(filename, 'rb') as csvfile:
	lines = csv.reader(csvfile, delimiter='|')
	features = dict()
	for line in lines:
	    controversial = True if (int(line[0])) == 1 else False
	    words = str(line[1]).split()
	    for word in words:
	        cleanword = (word.translate(None, string.punctuation)).lower()
	        if (features.has_key(cleanword)):
	            scores = features[cleanword]
	            scores = modScores(scores, controversial)
	            features[cleanword] = scores
	        else:
	            scores = modScores([0, 0], controversial)
	            features[cleanword] = scores
    return features
        
def nb(totPercentCont, totPercentClean):
    with open("output/freqTable.csv", 'rb') as csvfile:
        	lines = csv.reader(csvfile, delimiter='|')
        	tupList = list()
	        for line in lines:
	            word = str(line[0])
	            pCont = float(line[3])
	            if pCont != 0:
	                confOfCont = ((totPercentCont * pCont) * totPercentCont) / pCont
	            else:
	                confOfCont = 0.0
	            tupList.append((word, confOfCont))
	        tupList.sort(key=lambda x: x[1])
	        out = csv.writer(open("output/out.csv","wb"), delimiter='|',quoting=csv.QUOTE_ALL)
	        for tup in tupList:
	            out.writerow([tup[0], tup[1]])
	            
	            
        
def printFreqTable(features):
    freqWriter = csv.writer(open("output/freqTable.csv","wb"), delimiter='|',quoting=csv.QUOTE_ALL)
    totCont = 0
    totClean = 0
    for key, value in features.iteritems():
        cont = int(value[0])
        clean = int(value[1])
        pCont = float(cont) / (float(cont) + float(clean))
        pClean = 1 - pCont
        freqWriter.writerow([key, str(cont), str(clean), str(pCont), str(pClean)])
        totCont += cont
        totClean += clean
    tot = totCont + totClean
    totPercentCont = float(totCont) / float(totClean)
    totPercentClean = 1 - totPercentCont
    print("Percent Controversial: " + str(totPercentCont) + " and Percent Clean: " + str(totPercentClean))
    nb(totPercentCont, totPercentClean)
        

features = getFeatures('output/training.csv')
printFreqTable(features)
print('created output/features.csv')