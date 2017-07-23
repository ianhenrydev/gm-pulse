import json, csv, codecs, os

def writeLine(comment, out):
	score = int(comment['data']['controversiality'])
	sentiment = ""
	if score == 0:
		sentiment = "pos"
	else:
		sentiment = "neg"
	body = (comment['data']['body'].encode('ascii', 'ignore')).replace('\n', ' ').replace('\r', '')
	out.writerow([body, sentiment])
	

def getReplies(parent, out):
	try:
		for comment in parent['data']['replies']['data']['children']:
			writeLine(comment, out)
			getReplies(comment, out)
	except Exception as e:
		pass
	return

def printThread(thread, out):
	with open(thread) as dataFile:
		jsonFile = json.load(dataFile)
		thread = jsonFile[0]['data']['children'][0]['data']['name']
		for comment in jsonFile[1]['data']['children']:
			try:
				writeLine(comment, out)
				getReplies(comment, out)
			except Exception as e:
				pass

directory = "soccer-data/"
out = csv.writer(open("output/training.csv","wb"), delimiter=',',quoting=csv.QUOTE_ALL)
files = os.listdir(directory)
for file in files:
	printThread(directory + file, out)
print('created output/training.csv')