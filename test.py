import nltk
import pickle

f = open('my_classifier1.pickle', 'rb')
classifier = pickle.load(f)
f.close()

def word_feats(words):
    return dict([(word, True) for word in words])

sw = nltk.corpus.stopwords.words('english')
# Predict
neg = 0
pos = 0
sentence = "nothing"
sentence = sentence.lower()
sentences = sentence.split('.')   # these are actually list of sentences

for sent in sentences:
    if sent != "":
        words = [word for word in sent.split(" ") if word not in sw]
        classResult = classifier.classify(word_feats(words))
        print(str(sent) + ' --> ' + str(classResult))