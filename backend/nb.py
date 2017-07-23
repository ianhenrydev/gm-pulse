from textblob.classifiers import NaiveBayesClassifier

with open('output/training.csv', 'r') as trainingFile:
    cl = NaiveBayesClassifier(trainingFile, format="csv")