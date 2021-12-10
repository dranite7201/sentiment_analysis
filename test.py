import nltk
import pickle
import string
from nltk import word_tokenize, sent_tokenize

f = open('my_classifier.pickle', 'rb')
classifier = pickle.load(f)
f.close()

def word_feats(words):
    return dict([(word, True) for word in words])
    
sw = nltk.corpus.stopwords.words('english')
sentence = "I am a good boy. I always hate you"
sentence = sentence.lower()
#sentences = sentence.split('.')   # these are actually list of sentences
en_stops=set(sw) 
tmp = []
classResults =[]
result=[]
tokenized_sentences = []
exclusion_set = en_stops.union(string.punctuation)

for sent in sent_tokenize(sentence):
    if sent != "":
        pos=0
        neg=0
        tokenized_sentences.append([word for word in word_tokenize(sent.lower()) if word not in exclusion_set])
        for word in tokenized_sentences:
            if(len(word)==0):
              continue
            classResult = classifier.classify(word_feats(word))
            if(classResult=='pos'):
                pos+=1
            else:
                neg+=1
        if (pos==neg):
            print(sent + '----->' + ' neutral')
        elif(pos>neg):
            print(sent + '----->' + ' pos')
        else:
            print(sent + '----->' + ' neg')