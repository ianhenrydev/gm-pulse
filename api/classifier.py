from textblob.classifiers import NaiveBayesClassifier
try:
   import cPickle as pickle
except:
   import pickle
import os, sys

def save_classifier(cl):
    print('saving classifier')
    f = open('output/classifier.pickle', 'wb')
    pickle.dump(cl, f, -1)
    f.close()

def load_classifier():
    print('loading classifier')
    f = open('output/classifier.pickle', 'rb')
    cl = pickle.load(f)
    f.close()
    return cl

def test_classifier(cl):
    print('testing classifier')
    with open('output/test.csv', 'r') as testFile:
        print(str(cl.accuracy(testFile)))

def get_classifier():
    if os.path.isfile('output/classifier.pickle'):
        cl = load_classifier()
    else:
        print('creating classifier')
        with open('output/training.csv', 'r') as trainingFile:
            cl = NaiveBayesClassifier(trainingFile, format="csv")
            save_classifier(cl)
    return cl

cl = get_classifier()
if len(sys.argv) > 1:
    prob_dist = cl.prob_classify(sys.argv[1])
    print("Class: " + str(prob_dist.max()))
    print("Pos prob: " + str(round(prob_dist.prob("pos"), 2)))
    print("Neg prob: " + str(round(prob_dist.prob("neg"), 2)))
else:
    test_classifier(cl)
