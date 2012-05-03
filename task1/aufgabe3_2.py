from nltk.book import *
from nltk.corpus import stopwords
import pylab
def con(text, stopwords):
    alfa = []
    content = [w for w in text if w.lower() not in stopwords and w.isalpha()]
    fdist = FreqDist(content)
    keys = fdist.keys()
    vals = fdist.values()
    maxiFreq = vals[0]
    for i in range(1, maxiFreq + 1):
	k = len([w for w in keys if fdist[w] == i])
	alfa.append(k)

    ys = range(1, maxiFreq + 1)
    xs = alfa
    pylab.xlabel("Anzahl der Woerter")
    pylab.ylabel("Haeufigkeit")
    pylab.plot(xs, ys)
    pylab.show()
 
    pylab.xlabel("Anzahl der Woerter log scale")
    pylab.ylabel("Haeufigkeit log scale")
    pylab.plot(xs, ys)
    pylab.xscale('log')
    pylab.yscale('log')
    pylab.show()		
    return alfa

con(text1, stopwords.words('english'))
con(text2, stopwords.words('english'))
