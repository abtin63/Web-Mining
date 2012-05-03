from nltk.book import *

def letterFrequ(text):
    freq_dist = FreqDist()
    for word in text:
        for char in word:
            if char.isalpha():
	        freq_dist.inc(char)

    freq_dist.plot(30)
    return freq_dist
    
print letterFrequ(text1)
print letterFrequ(text2)
