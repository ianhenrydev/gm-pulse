import csv

def modScores(scores, controversial):
    if (controversial):
        scores[0] = int(scores[0]) + 1
    else:
        scores[1] = int(scores[1]) + 1
    return scores

def getFeatures(filename):
    with open('training.csv', 'rb') as csvfile:
	lines = csv.reader(csvfile, delimiter='|')
	features = dict()
	for line in lines:
	    controversial = True if (int(line[0])) == 1 else False
	    words = str(line[1]).split()
	    for word in words:
	        if (features.has_key(word.lower())):
	            scores = features[word.lower()]
	            scores = modScores(scores, controversial)
	            features[word.lower()] = scores
	        else:
	            scores = modScores([0, 0], controversial)
	            features[word.lower()] = scores
    return features

def getPercentages(features):
    stats = dict()
    percents = dict()
    high = ""
    highscore = 0.0
    for key, value in features.iteritems():
        controversial = int(value[0])
        clean = int(value[1])
        total = controversial + clean
        percentControversial = float(controversial) / float(total)
        if percentControversial > highscore:
            high = key
        stats[key] = [total, controversial, clean]
        percents[key] = percentControversial
    sortedPercents =sorted(percents.items(), key=lambda x:x[1])
    out = csv.writer(open("features.csv","wb"), delimiter='|',quoting=csv.QUOTE_ALL)
    for x in sortedPercents:
        out.writerow([x[0], x[1], stats[x[0]][0], stats[x[0]][1], stats[x[0]][2]])

features = getFeatures('training.csv')
getPercentages(features)
print('done')