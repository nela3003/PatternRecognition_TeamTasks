# Imports
import numpy as np
import matplotlib.pyplot as plt

# Change the default colormap to gray
plt.rcParams['image.cmap'] = 'gray'


# id is a string of the format XXX-YY-ZZ where
#   XXX = document number
#    YY = line number
#    ZZ = word number
#
# transcript is a string containing the transcription of the word on a character basis

class Word:
    def __init__(self, id, transcript):
        self.docNr = id[0:3]
        self.lineNr = id[4:6]
        self.wordNr = id[7:9]
        self.img = plt.imread('./Exercise_3/data/cropped_words/'+id+'.jpg')
        self.transcript = transcript


wordlist = list()

with open('./Exercise_3/data/ground-truth/transcription.txt') as f:
    for line in f:
        id, transcript = str.split(line, " ")
        wordlist.append(Word(id, transcript))
