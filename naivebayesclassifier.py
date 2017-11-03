# Naive Bayes Classifier
import re
import math

# return unique set of words from document.
def getwords(document):
    splitter = re.compile('[^a-zA-Z]')
    # split words by non-alpha characters.
    words = [word.lower() for word in splitter.split(document)
                 if len(word) > 2 and len(word) < 20]
    return dict([(feature,1) for feature in words])

class naivebayesclassifer:
    def __init__(self, getfeatures):
        # feature/category.
        self.fcat = {}
        # document/category.
        self.dcat = {}
        self.extractfeatures = getfeatures

    # increment feature count in a category.
    def incrementfcat(self, feature, category):
        self.fcat.setdefault(feature, {})
        self.fcat[feature].setdefault(category, 0)
        self.fcat[feature][category] += 1

    # increment document count in a category.
    def incrementdcat(self, category):
        self.dcat.setdefault(category, 0)
        self.dcat[category] += 1

    # count of feature in a category.
    def fcatcount(self, feature, category):
        if feature in self.fcat and category in self.fcat[feature]:
            return float(self.fcat[feature][category])
        return 0.0

    # count of documents in a category.
    def dcatcount(self, category):
        if category in self.dcat:
            return float(self.dcat[category])
        return 0.0

    # train the classifier.
    def train(self, document, category):
        features = self.extractfeatures(document)
        for feature in features:
            self.incrementfcat(feature, category)
        self.incrementdcat(category)

    # Pr(Feature|Category)
    def featureprobability(self, feature, category):
        if self.dcatcount(category) == 0:
            return 0
        return self.fcatcount(feature,category)/self.dcatcount(category)

    # Weighted Pr(Feature|Category).
    def weightedprobability(self, feature, category):
        weight = 1.0
        assumedprob = 0.5
        basicprob = self.featureprobability(feature, category)
        featurecount = sum([self.fcatcount(feature, cat) for cat in self.dcat.keys()])
        weightprob = ((weight*assumedprob)+(featurecount*basicprob))/(weight+featurecount)
        return weightprob

    # Pr(Document|Category)
    # assuming individual probs are independent of each other.
    def documentprobability(self, document, category):
        features = self.extractfeatures(document)
        prob = 1
        for feature in features:
            prob *= self.weightedprobability(feature, category)
        return prob

    # Pr(Category|Document) = Pr(Document|Category)*Pr(Cateogory)/Pr(Document)
    # denominator can be ignored as we are going to compare probs.
    def probability(self, document, category):
        catprob = self.dcatcount(category)/sum(self.dcat.values())
        docprob = self.documentprobability(document, category)
        return docprob*catprob

    # classify the documents.
    def classify(self, document):
        probs = {}
        # find category with highest probability.
        highestprob = 0.0
        for cat in self.dcat.keys():
            probs[cat] = self.probability(document, cat)
            if probs[cat] > highestprob:
                highestprob = probs[cat]
                rescat = cat
        return rescat

if __name__ == '__main__':
    cl = naivebayesclassifer(getwords)
    cl.train('time is the most valuable thing in this world', 'good')
    cl.train('it is such a waste of time and money', 'bad')
    cl.train('python is very good programming language', 'good')
    cl.train('casio is a good source of money', 'bad')
    cl.train('knowing different languages is sign of intelligence', 'good')
    print (cl.classify('what are some good languages to learn for earning money'))
