import json, csv, codecs, os

def writeLine(comment, out, thread):
	score = int(comment['data']['controversiality'])
	body = (comment['data']['body'].encode('ascii', 'ignore')).replace('\n', ' ').replace('\r', '')
	out.writerow([score, body, thread])

def getReplies(parent, out, thread):
	try:
		for comment in parent['data']['replies']['data']['children']:
			writeLine(comment, out, thread)
			getReplies(comment, out, thread)
	except Exception as e:
		pass
	return

def printThread(thread, out):
	with open(thread) as dataFile:
		jsonFile = json.load(dataFile)
		thread = jsonFile[0]['data']['children'][0]['data']['name']
		for comment in jsonFile[1]['data']['children']:
			try:
				writeLine(comment, out, thread)
				getReplies(comment, out, thread)
			except Exception as e:
				pass

out = csv.writer(open("training.csv","wb"), delimiter='|',quoting=csv.QUOTE_ALL)
#out.writerow(["score", "body", "thread"])
files = os.listdir("data")
for file in files:
	printThread("data/" + file, out)