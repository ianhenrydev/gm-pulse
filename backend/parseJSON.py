import json, csv, codecs, os
from random import randint

def writeLine(comment, out, testOut):
	score = int(comment['data']['controversiality'])
	sentiment = ""
	if score == 0:
		sentiment = "pos"
	else:
		sentiment = "neg"
	body = (comment['data']['body'].encode('ascii', 'ignore')).replace('\n', ' ').replace('\r', '')
	if randint(0, 3) == 0:
		testOut.writerow([body, sentiment])
	else:
		out.writerow([body, sentiment])
	

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

directory = "smol/"
out = csv.writer(open("output/training.csv","wb"), delimiter=',',quoting=csv.QUOTE_ALL)
testOut = csv.writer(open("output/test.csv","wb"), delimiter=',',quoting=csv.QUOTE_ALL)
files = os.listdir(directory)
for file in files:
	printThread(directory + file, out, testOut)
print('created output/training.csv')