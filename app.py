from flask import Flask, render_template, flash, request, redirect, url_for
import pickle
import nltk
import matplotlib as plt

app = Flask(__name__)

#get classifier model
f = open('my_classifier1.pickle', 'rb')
classifier = pickle.load(f)
f.close()

#put word inside a feature
def word_feats(words):
    return dict([(word, True) for word in words])



@app.route('/')
def upload_form():
	return render_template('upload.html')


@app.route('/result', methods=["POST","GET"])
def classify():
	if request.method == "POST":
		sentence = request.form['text']
		p=0
		n=0
		neu=0
		sw = nltk.corpus.stopwords.words('english')
		sentence = sentence.lower()
		sentences = sentence.split('.')  
		results = []
		for sent in sentences:
			if sent != "":
				pos=0
				neg=0
				tmp = []
				words = [word for word in sent.split() if word not in sw]
				for word in words:
					tmp.append(word)
					classResult = classifier.classify(word_feats(tmp))
					if(classResult=='pos'):
						pos+=1
					else:
						neg+=1
				if (pos==neg):
					l = [sent,"Neutral"]
					results.append(l)
					neu+=1
				elif(pos>neg):
					l = [sent,"Positive"]
					results.append(l)
					p+=1
				else:
					l = [sent,"Negative"]
					results.append(l)	
					n+=1	
		sumv = n+p+neu
		datas = [p/sumv*100,n/sumv*100,neu/sumv*100]
		labels= ['positive', 'negative', 'neutral']
		return render_template('result.html', results=results, datas=datas, labels=labels)
	return render_template('upload.html')

if __name__ == "__main__":
	app.run(debug=True)
