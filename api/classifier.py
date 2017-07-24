from textblob.classifiers import NaiveBayesClassifier
try:
   import cPickle as pickle
except:
   import pickle
import os, sys, json

def save_classifier(cl):
    f = open('output/classifier-smol.pickle', 'wb')
    pickle.dump(cl, f, -1)
    f.close()

def load_classifier():
    f = open('output/classifier-smol.pickle', 'rb')
    cl = pickle.load(f)
    f.close()
    return cl

def test_classifier(cl):
    with open('output/test.csv', 'r') as testFile:
        print(str(cl.accuracy(testFile)))

def get_classifier():
    if os.path.isfile('output/classifier-smol.pickle'):
        cl = load_classifier()
    else:
        with open('output/training.csv', 'r') as trainingFile:
            cl = NaiveBayesClassifier(trainingFile, format="csv")
            save_classifier(cl)
    return cl

cl = get_classifier()
if len(sys.argv) > 1:
    prob_dist = cl.prob_classify(sys.argv[1])
    print json.dumps({ "class": prob_dist.max(), "pos_prob": round(prob_dist.prob("pos"), 2), "neg_prob": round(prob_dist.prob("neg"), 2)}, sort_keys=True)
else:
    test_classifier(cl)
