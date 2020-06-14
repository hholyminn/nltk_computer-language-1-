################################################################
################ Just Change this sections #####################
################################################################
# (1) Type Your Sentence

sent = "The professor permitted the students to take a nap during the class."

# (2) Make your CFG file for parsing your sentence.

# ex. grammar.cfg (see the direction in the powerpoint)

################################################################

import nltk
grammar = nltk.data.load("file:.\\grammar5.cfg")
parser = nltk.ChartParser(grammar)
tokens = nltk.tokenize.word_tokenize(sent)
trees = parser.parse(tokens)

with open(".\\result.txt", "w") as f1:
    for tree in trees:
        print(tree)
        f1.write(str(tree)+"\n\n")
        tree.draw()

