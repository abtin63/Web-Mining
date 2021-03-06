from nltk.book import *
import pylab
def letterFrequ(text):
    in_word_bigrams = FreqDist()
    content = [w for w in text if w.isalpha()]
    for word in content:
        for bi in bigrams(word):
            in_word_bigrams.inc("".join(bi))
    
    in_word_bigrams.plot(30)
    return  in_word_bigrams
    
print letterFrequ(text1)
print letterFrequ(text2)

