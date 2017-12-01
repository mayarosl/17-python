import sys

# read our corpus
corpus = sys.stdin.read()

# start every sentence from a new line 
corpus = corpus.replace (". ", ".\n")
# to prevent extra-split
corpus = corpus.replace (':\n', ': ')
# split on every new line
corpus = corpus.split ('\n')

# counter for sentence indexing
index = 1

# create an empty list to keep all sentences from the corpus
sents = []

# start loop which adds sentences from corpus to our new list 
for sent in corpus:
    if sent not in ' ': # do not add empty lines
        sents.append (sent)
# print sentences from the list one by one
for sent in sents:
    print ('\n', '# text_id = %s' % (index), '# text = %s' % (sent), sep = '\n')
# a head of the future "table"
    print ('ID', 'FORM', 'LEMMA', 'UPOSTAG', 'XPOSTAG', 'FEATS', 'HEAD', 'DEPREL', 'DEPS', 'MISC', sep = '\t')

    # a counter for tokens in every sentence
    n = 1
    tokens = sent.split(' ')
    # empty list for our tokens
    tkns = []
    # add tokens into our new list without puctuation marks
    for token in tokens:
        token = token.strip('.,:;()!?')
        if token not in tkns:
            tkns.append (token)
    # print counter, token and future places for annotation 
    for token in tokens:
            print (n, token, '-', '-', '-', '-', '-', '-', '-', '-', sep = '\t')
            # increase counter for token
            n = n+1
    #increase counter for sentence
    index = index+1
