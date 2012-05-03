from nltk.book import *
from nltk.corpus import stopwords
import pylab
def zipfPlot(text, stopwords):
    content = [w for w in text if w.lower() not in stopwords and w.isalpha()]
    fdist = FreqDist(content)
    vals = fdist.values()
    pylab.xlabel("Rang")
    pylab.ylabel("Haeufigkeit")
    pylab.plot(range(1, 31), vals[:30])
    pylab.show()
    
    pylab.xlabel("Rang log scale")
    pylab.ylabel("Haeufigkeit log scale")
    pylab.plot(range(1, 31), vals[:30])
    pylab.xscale('log')
    pylab.yscale('log')
    pylab.show()

zipfPlot(text1, stopwords.words('english'))
zipfPlot(text2, stopwords.words('english'))
