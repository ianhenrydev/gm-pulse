from textblob.classifiers import NaiveBayesClassifier
try:
   import cPickle as pickle
except:
   import pickle
import os

def save_classifier(cl):
    print('saving classifier')
    f = open('output/semtiment_classifier.pickle', 'wb')
    pickle.dump(cl, f, -1)
    f.close()

def load_classifier():
    print('loading classifier')
    f = open('output/semtiment_classifier.pickle', 'rb')
    cl = pickle.load(f)
    f.close()
    return cl

def test_classifier(cl):
    with open('output/test.csv', 'r') as testFile:
        print(str(cl.accuracy(testFile)))

def get_classifier():
    if os.path.isfile('output/semtiment_classifier.pickle'):
        cl = load_classifier()
    else:
        print('creating classifier')
        with open('output/training.csv', 'r') as trainingFile:
            cl = NaiveBayesClassifier(trainingFile, format="csv")
            save_classifier(cl)
    return cl

cl = get_classifier()
test_classifier(cl)