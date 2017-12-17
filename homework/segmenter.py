import sys

corpus = sys.stdin.read()
corpus = corpus.replace ('. ', '.\n')

print (corpus)
#sys.stdout.write(corpus)
