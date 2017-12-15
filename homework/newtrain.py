import sys
# head for table
print ('#P', 'count', 'tag', 'form', sep = '\t')

# dict to count tags frequency
tagsfreq = {}
# dict and counter to count n of tokens
formfreq = {}
counter = 0
# dict to find freq of w=t pairs
wt = {}

# read the file line by line:
for line in sys.stdin.readlines():
	# we do not take comments (e.g. head of tables):
	if line [0] == '#':
		continue
	# if there is no tab char, skip the line
	if '\t' not in line:
		continue
	# make a list of the cells in the row
	row = line.split('\t')
	# if there are not 10 cells, skip the line
	if len(row) != 10:
		continue
	# the form is the value of the 2nd cell (+make chat-s small)
	form = row[1]
	form = form.lower()
	# the tag is the value of the 4th cell
	tag = row[3]

	# matrix 'wt' to count the frequency of a word=tag pairs
	if form not in wt:
		wt[form] = {}
	if tag not in wt[form]:
		wt[form][tag] = 0
	wt[form][tag] = wt[form][tag] + 1

	# here we count tags frequency (in dict 'tagsfreq')
	if tag not in tagsfreq:
		tagsfreq[tag] = 0
	tagsfreq[tag] = tagsfreq[tag] + 1

	# here we count freq of tokens (in dict 'tokens')
	if form not in formfreq:
		formfreq[form] = 0
	formfreq[form] = formfreq[form] + 1
	
	# increase word's counter on every step since there is only one word per line
	counter = counter + 1

# ---------for the final output-----------------

for tag in tagsfreq:
	print ('%.2f'%(tagsfreq[tag]/counter), tagsfreq[tag], tag, '-', sep = '\t')

for frm in wt:
	for tg in wt[frm]:
		print ('%.2f'% (wt[frm][tg]/formfreq[frm]), wt[frm][tg], tg, frm, sep = '\t') 

