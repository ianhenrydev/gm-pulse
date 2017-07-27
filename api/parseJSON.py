import json, csv, codecs, os, sys
from random import randint

isTrain = True
posCount = 0
negCount = 0
count = 0
evenData = False

def write(comment, sentiment):
	body = (comment['data']['body'].encode('ascii', 'ignore')).replace('\n', ' ').replace('\r', '')
	out.writerow([body, sentiment])
	global count
	count += 1
	#if count >= 2000:
		#sys.exit()

def writeLine(comment, out, testOut):
	global posCount, negCount, evenData
	score = int(comment['data']['controversiality'])
	sentiment = ""
	if score == 0:
		sentiment = "pos"
		posCount += 1
		write(comment, sentiment)
	else:
		sentiment = "neg"
		negCount += 1
		write(comment, sentiment)
	

def getReplies(parent, out, testOut):
	try:
		for comment in parent['data']['replies']['data']['children']:
			writeLine(comment, out, testOut)
			getReplies(comment, out, testOut)
	except Exception as e:
		pass
	return

def printThread(thread, out, testOut):
	with open(thread) as dataFile:
		jsonFile = json.load(dataFile)
		thread = jsonFile[0]['data']['children'][0]['data']['name']
		for comment in jsonFile[1]['data']['children']:
			try:
				writeLine(comment, out, testOut)
				getReplies(comment, out, testOut)
			except Exception as e:
				pass

if len(sys.argv) > 1:
	evenData = True
else:
	evenData = False
directory = "soccer-data/"
if evenData:
	trainLocation = "train-even"
	testLocation = "test-even"
else:
	trainLocation = "train"
	testLocation = "test"
out = csv.writer(open("output/" + trainLocation + ".csv","wb"), delimiter=',',quoting=csv.QUOTE_ALL)
testOut = csv.writer(open("output/" + testLocation + ".csv","wb"), delimiter=',',quoting=csv.QUOTE_ALL)
files = os.listdir(directory)
for file in files:
	printThread(directory + file, out, testOut)
print('created output/training.csv')