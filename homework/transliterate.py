import sys

# first - create a dict 'table' from table with turkish-russian symbols
table = {}

# open txt file with our symbols

a = open (sys.argv[1])
symbols = a.readlines()
a.close()

# read out new variable with symbols line by line
for line in symbols:
	# remove new line symbol at the end of the line
	line = line.replace('\n', '')
	# make a list of symbols correspondencies
	pair = line.split ('\t')
	# turkish symbol is the 1st cell
	tur = pair [0]
	# russian symbol is the 2nd cell
	rus = pair [1]
	# add the symbols into dict, tur is a key, rus is a value
	if tur not in table:
		table [tur] = rus

# -----------now we are ready for transliteration------------------

# we work with input file
original_corpus = sys.stdin.readlines()

# read original text line by line
for line in original_corpus:
	if '\t' in line:
		row = line.split('\t')
		if len(row) != 10:
			continue
		if '#' in row[0]:
			sys.stdout.write (line)	
		else:
			form = row [1]
			translit = row [9]
			newtranslit = 'translit='

			# look at every symbol in the form:
			for orig_smb in form:
				# if our symbol is in the table:
				if orig_smb in table:
					# new variable of that new symbol
					new_smb = table[orig_smb]
				# if symbol not in the table (e.g. numbers, punctuation), use our old symbol:
				else:	
					new_smb = orig_smb
				# add resulted symbol (new or old) into temporal string
				newtranslit = newtranslit + new_smb
			# add '\n' for correct output
			newtranslit = newtranslit + '\n'
			#print (form, newtranslit) #- до этого момента все работает
			transliterated_line = line.replace (translit, newtranslit)
			# write our new line into our new file
			sys.stdout.write (transliterated_line)
		
			
	else:
		sys.stdout.write (line)
