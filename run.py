# import gensim

# # Load Google's pre-trained Word2Vec model.
# gensim.models.KeyedVectors.load_word2vec_format("GoogleNews-vectors-negative300.bin.gz", binary=True)

# from gensim import models

# w = models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)

import gensim
from gensim import models
import logging

# Logging code taken from http://rare-technologies.com/word2vec-tutorial/
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

print("trying its best 1")
# model = gensim.models.Word2Vec.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)  
model = models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)

# Does the model include stop words?
print("trying its best 2")
print(model.get_vecattr(key, attr))
# print("Does it include the stop words like \'a\', \'and\', \'the\'? %d %d %d" % ('a' in model.vocab, 'and' in model.vocab, 'the' in model.vocab))

# Retrieve the entire list of "words" from the Google Word2Vec model, and write
# these out to text files so we can peruse them.
vocab = model.vocab.keys()

fileNum = 1

wordsInVocab = len(vocab)
wordsPerFile = int(100E3)

# Write out the words in 100k chunks.
for wordIndex in range(0, wordsInVocab, wordsPerFile):
    # Write out the chunk to a numbered text file.    
    with open("vocabulary/vocabulary_%.2d.txt" % fileNum, 'w') as f:
        # For each word in the current chunk...        
        for i in range(wordIndex, wordIndex + wordsPerFile):
            # Write it out and escape any unicode characters.            
            f.write(vocab[i].encode('UTF-8') + '\n')
    
    fileNum += 1