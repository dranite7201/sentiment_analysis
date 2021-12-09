import nltk
import pickle

f = open('my_classifier.pickle', 'rb')
classifier = pickle.load(f)
f.close()

def word_feats(words):
    return dict([(word, True) for word in words])

neg = 0
pos = 0
sentence = "absolutely nothing. awesome movie. bad movie ever"
sw = nltk.corpus.stopwords.words('english')
sentence = sentence.lower()
sentences = sentence.split('.')  

results = []
for sent in sentences:
    if sent != "":
        pos=0
        neg=0
        tmp = []
        words = [word for word in sent.split(" ") if word not in sw]
        for word in words:
            tmp.append(word)
            classResult = classifier.classify(word_feats(tmp))
            if(classResult=='pos'):
                pos+=1
            else:
                neg+=1
        if (pos==neg):
            l = [sent,"neutral"]
            results.append(l)
        elif(pos>neg):
            l = [sent,"pos"]
            results.append(l)
        else:
            l = [sent,"neg"]
            results.append(l)
print(results)