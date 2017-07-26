from textblob.classifiers import DecisionTreeClassifier
try:
   import cPickle as pickle
except:
   import pickle
import os, sys, json, numpy

def save_classifier(cl):
    print str('saving classifier')
    f = open('output/classifier-tree.pickle', 'wb')
    pickle.dump(cl, f, -1)
    f.close()

def load_classifier():
    print str('loading classifier')
    f = open('output/classifier-tree.pickle', 'rb')
    cl = pickle.load(f)
    f.close()
    return cl

def test_classifier(cl):
    with open('output/test.csv', 'r') as testFile:
        print(str(cl.accuracy(testFile)))
        print(str(cl.show_informative_features(10)))

def get_classifier():
    print str('getting classifier')
    if os.path.isfile('output/classifier-tree.pickle'):
        cl = load_classifier()
    else:
        print str('creating classifier')
        with open('output/training.csv', 'r') as trainingFile:
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
