import sys

wt = {} # dict to contain word=tag mapping
mostfreqtag = {} # dict to find the most freq tag
mft_list = [] # list to reverse and find the most freq tag

# Open model to find out the most frequent tag
a = open (sys.argv[1])
model = a.readlines()
a.close()

for line in model:
	# if there is no tab character, skip the line
	if '\t' not in line:
		continue
	# if line is a comment, skip it
	if line [0] == '#':
		continue
	# make a list of the cells in the row
	row = line.split('\t')
	# if there are not 4 cells, skip the line
	if len(row) != 4:
		continue
	# the form is the value of the last cell
	form = row[3]
	form = form.strip('\n') 
	# the tag is the value of the 3d cell
	tag = row[2]
	tag = tag.strip('\n')
	# frequency
	n = row[1]
	# probability
	p = row [0]
	p = float (p) #convert string into num

	# loop through the all FORMS in TRAIN and make a new dict we do not take lines without forms
	if form != '-':	 # ------------эта часть кода - для строк с формами------------
		tp_counter = 0
		# if we have not seen form yet in out word=tag dict		
		if form not in wt:
			wt[form] = tag
			tp_counter = p
		else:
			if p >= tp_counter:
				wt [form] = tag
			else:
				continue
			 
	else: 	#---------- этa часть кода для работы со строчками без форм, только тэги-----
		if tag not in mostfreqtag:
			mostfreqtag[tag] = n
		#-----------------------------------------------------------------------		

# most freq tag
for t in mostfreqtag:
	mft_list.append ((int(mostfreqtag[t]), t))
mft_list.sort(reverse = True)	
mft = mft_list[0][1]



#----------TAGGER---------------------------------------

# now read our input
doc = sys.stdin.readlines()

for line in doc:
	if '\t' in line:
		row = line.split('\t')
		if len(row) != 10:
			continue
		if '#' in row[0]:
			sys.stdout.write(line)
		else:	
			if row[3] != '-':
				sys.stdout.write(line)
			else:
				n = row [0]
				w = row[1]
				t = row [3]
				translit = row [9]
				newt = '!'
			
				if w in wt:
					newt = wt[w]
				else:
					newt = mft

				tagged_line = n+'\t'+ w +'\t'+ '-'+'\t'+newt+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+translit
				sys.stdout.write (tagged_line)
	
	else:
		sys.stdout.write (line)

