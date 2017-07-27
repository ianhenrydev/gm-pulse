from textblob.classifiers import DecisionTreeClassifier
try:
   import cPickle as pickle
except:
   import pickle
import os, sys, json, csv

def save_classifier(cl):
    print str('saving classifier')
    f = open('output/classifier-random-tree.pickle', 'wb')
    pickle.dump(cl, f, -1)
    f.close()

def load_classifier():
    print str('loading classifier')
    f = open('output/classifier-random-tree.pickle', 'rb')
    cl = pickle.load(f)
    f.close()
    return cl

def test_classifier(cl):
    out = csv.writer(open("output/results-random-tree.csv","wb"), delimiter=',',quoting=csv.QUOTE_ALL)
    out.writerow(['text', 'class', 'predict', 'pos_conf', 'neg_conf'])
    with open('output/test-even.csv', 'r') as testFile:
        #print str(cl.accuracy(testFile))
        testReader = csv.reader(testFile, delimiter=',', quotechar='"')
        for row in testReader:
            prob_dist = cl.classify(row[0])
            outrow = [row[0], row[1], prob_dist]
            out.writerow(outrow)

def get_classifier():
    print str('getting classifier')
    if os.path.isfile('output/classifier-random-tree.pickle'):
        cl = load_classifier()
    else:
        print str('creating classifier')
        with open('output/train-even.csv', 'r') as trainingFile:
            cl = DecisionTreeClassifier(trainingFile, format="csv")
            save_classifier(cl)
    return cl

cl = get_classifier()
if len(sys.argv) > 1:
    print str('classifying string')
    prob_dist = cl.prob_classify(sys.argv[1])
    print str(sys.argv[1])
    print str(prob_dist.max())
    print str(round(prob_dist.prob("pos"), 2))
    print str(round(prob_dist.prob("neg"), 2))
else:
    print str('testing classifier')
    test_classifier(cl)
