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

def getPercentages(features):
    stats = dict()
    percents = dict()
    high = ""
    highscore = 0.0
    for key, value in features.iteritems():
        controversial = int(value[0])
        clean = int(value[1])
        total = controversial + clean
        if (total >= 3):
            percentControversial = float(controversial) / float(total)
            if percentControversial > highscore:
                high = key
            stats[key] = [total, controversial, clean]
            percents[key] = percentControversial
    sortedPercents =sorted(percents.items(), key=lambda x:x[1])
    out = csv.writer(open("output/features.csv","wb"), delimiter='|',quoting=csv.QUOTE_ALL)
    for x in sortedPercents:
        out.writerow([x[0], x[1], stats[x[0]][0], stats[x[0]][1], stats[x[0]][2]])

features = getFeatures('output/training.csv')
getPercentages(features)
print('done')