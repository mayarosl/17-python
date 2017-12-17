import sys
import string

# read our corpus
corpus = sys.stdin.read()

# start a new line after every fulstop
#corpus = corpus.replace (". ", ".\n")
# to prevent extra-split
corpus = corpus.replace (':\n', ': ')
corpus = corpus.replace (';\n', '; ')

# split on every new line
corpus = corpus.split ('\n')

# counter for sentence indexing
index = 1

# create an empty list to keep all sentences from the corpus
sents = []

# start the loop which adds sentences from corpus to our new empty list 
for sent in corpus:
	if sent not in ' ': # do not add empty lines
		sents.append (sent)

# print sentences from the list one by one
for sent in sents:
	print ('# text_id = %s' % (index), '# text = %s' % (sent), sep = '\n')
	#out1 = '# text_id = %s' % (index)+'\n'+'# text = %s' % (sent)+'\n'
	#sys.stdout.write(out1)
	# a head of the future "table"
	print ('# ID', 'FORM', 'LEMMA', 'UPOSTAG', 'XPOSTAG', 'FEATS', 'HEAD', 'DEPREL', 'DEPS', 'MISC', sep = '\t')
	#out2 = '# ID'+'\t'+'FORM'+'\t'+'LEMMA'+'\t'+'UPOSTAG'+'\t'+'XPOSTAG'+'\t'+'FEATS'+'\t'+'HEAD'+'\t'+'DEPREL'+'\t'+'DEPS'+'\t'+'MISC'+'\n'
	#sys.stdout.write (out2)

	# to separate punctuation form words
	sent = sent.replace ('.', ' .')
	sent = sent.replace (',', ' ,')
	sent = sent.replace ('(', ' (')
	sent = sent.replace (')', ' )')
	sent = sent.replace (';', ' ;')
	sent = sent.replace (':', ' :')
	sent = sent.replace ('!', ' !')
	sent = sent.replace ('?', ' ?')	

	# split every sentence into list of tokens
	tokens = sent.split(' ')
	
	# empty list for our tokens
	tkns = []

	# a counter for every token in the sentence
	n = 1

	# add tokens into our new list
	for token in tokens:
		if token not in tkns:
			tkns.append (token)
	# print counter, token and future places for annotation 
	for token in tokens:
		#print (n, token, '-', '-', '-', '-', '-', '-', '-', '-', sep = '\t')
		out3 = str(n)+'\t'+token+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\n'
		# increase counter for token
		sys.stdout.write(out3)
		n = n+1
	#increase counter for sentence
	index = index+1
	sys.stdout.write ('\n')
	
