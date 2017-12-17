# georgian - ipa mapping table is stored in ge_table.txt


import sys

# first - create a dict 'table' from table with georgian-IPA symbols
table = {}

# open txt file with our symbols
my_symbols = open (sys.argv[1])
symbols = my_symbols.readlines()
my_symbols.close()

# read out new variable with symbols line by line
for line in symbols:
	# remove new line symbol at the end of the line
	line = line.replace('\n', '')
	# make a list of symbols correspondencies
	pair = line.split ('\t')
	# georgian symbol is the 1st cell
	ge = pair [0]
	# ipa symbol is the 2nd cell
	ipa = pair [1]
	# add the symbols into dict, ge is a key, ipa is a value
	if ge not in table:
		table [ge] = ipa

#---------------------------------

ge_text = sys.stdin.read() #string
ge_text = ge_text.replace ('. ', '.\n') # string with '\n'
ge_text = ge_text.split ('\n') # split string into list


for line in ge_text:
	
	if line not in ' ': # if not empty
		print ('Original sentence: ', line) # first print original sentence form our input file

		ipa_line = 'IPA transliteration: ' #here we will add transliterated words
	
		words = line.split() # split every line into list of words 

		for w in words: # for every element of our new list
			ipa_w = '' # new line for future transliterated word
			for smb in w: # for every symbol in the word
				if smb in table: # if symbol is in our table of mapping
					ipa_smb = table[smb] # set new symbol
				else:
					ipa_smb = smb # or just copy it (e.g. for numerals and punctuation)
				ipa_w = ipa_w + ipa_smb	# add every symbol to empty line
			ipa_w = ipa_w + ' ' #add a space after transliterated word
			ipa_line = ipa_line + ipa_w # add a word into line
		print (ipa_line, '\n') #print out the line 

