import sys
# head for table
print ('#P', 'count', 'tag', 'form', sep = '\t')

# dict to count tags frequency
tagsfreq = {}
# list and counter to count n of tokens
tokens = []
counter = 0
# dict to find freq of w=t pairs
wt = {}

# read the file line by line:
for line in sys.stdin.readlines():
	# if there is no tab char, skip the line
	if '\t' not in line:
		continue
	# make a list of the cells in the row
	row = line.split('\t')
	# if there are not 10 cells, skip the line
	if len(row) != 10:
		continue
	# the form is the value of the 2nd cell (+ make char-s small)
	form = row[1]
	form = form.lower()
	# the tag is the value of the 4th cell
	tag = row[3]


	# here we count tags frequency (in dict 'tagsfreq')
	if tag not in tagsfreq:
		tagsfreq[tag] = 0
	tagsfreq[tag] = tagsfreq[tag] + 1

	# here we count number of tokens (in list 'tokens')
	if form not in tokens:
		tokens.append(form)
		counter = counter + 1

	# matrix 'wt' to count the frequency of a word=tag pairs
	if form not in wt:
		wt[form] = {}
	if tag not in wt[form]:
		wt[form][tag] = 0
	wt[form][tag] = wt[form][tag] + 1

	# counter 'tot' for total number of instances of the word 
	for form in wt:
		tot = 0
		for tag in wt[form]:
			tot = tot + wt[form][tag]
	# p for w=t pairs
			p_wt = wt[form][tag] / tot

# ---------for the final output-----------------

for form in wt:
	print ('%.2f\t' % (p_wt), end='')
	for tag in wt[form]:
		print ('%d\t' % (wt[form][tag]), end='')
	print ('%s\t' % (tag), end='')
	print ('%s\t' % (form), end='')
	print ('')

	
for tag in tagsfreq:
	print ('%.2f'%(tagsfreq[tag]/counter), tagsfreq[tag], tag, '-', sep = '\t')


