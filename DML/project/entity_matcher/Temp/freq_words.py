from collections import Counter
from string import punctuation
import nltk

nltk.download()

def common_words():
    import nltk
    allWords = nltk.tokenize.word_tokenize("elec_pairs_stage1.txt")
    allWordDist = nltk.FreqDist(w.lower() for w in allWords)
    
    stopwords = nltk.corpus.stopwords.words('english')
    allWordExceptStopDist = nltk.FreqDist(w.lower() for w in allWords if w not in stopwords)   
    
    mostCommon= allWordDist.most_common(10).keys()
    
    return allWordExceptStopDist , mostCommon


def content_text(text = "elec_pairs_stage1.txt"):
    
    stopwords = set(nltk.corpus.stopwords.words('english')) # 0(1) lookups
    with_stp = Counter()
    without_stp  = Counter()

    with open(text) as f:
        for line in f:
            spl = line.split()
            # update count off all words in the line that are in stopwrods
            with_stp.update(w.lower().rstrip(punctuation) for w in spl if w.lower() in stopwords)
               # update count off all words in the line that are not in stopwords
            without_stp.update(w.lower().rstrip(punctuation)  for w in spl if w  not in stopwords)
    # return a list with top ten most common words from each 
    return [x for x in with_stp.most_common(10)],[y for y in without_stp.most_common(10)]
    
if __name__ == "__main__":
    print content_text("elec_pairs_stage1.txt")
    print common_words()