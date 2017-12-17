## From Georgian script to IPA

Georgian is one of Kartvelian languages, a language family indigenous to the Caucasus. Georgian is written in its own writing system, the Georgian script. The modern Georgian script, *Mkhedruli*, has been in use since the 11th century. There are 28 phonemic consonants in Standard Georgian, and 5 vowels[1].

IPA is an abbreviation for [The International Phonetic Alphabet](www.internationalphoneticassociation.org). It is an alphabetic system of phonetic notation aimed to illustrate a standardized representation of the sounds of spoken language.

OFFICIAL SOURCE??? LINK

### Propject

***First step*** is a table of Georgian → IPA symbols mapping. The file consists of two columns separated by a tab `\t` character.
A table looks simplistic due to several points. First, there are no capital letters in Georgian. Second, there is a one-to-one correspondence between the alphabetic symbols and phonemic sounds. 

It looks like:
```
	ა	ɑ
	ბ	b
	გ	g
	... 
```

The table is stored in ``ge_table.txt``.

***Second step*** is a code itself. 
- We reading the `ge_table.txt` and form the dictionary of Georgian → IPA symbols mapping.
```
import sys
table = {}

my_symbols = open (sys.argv[1])
symbols = my_symbols.readlines()
my_symbols.close()

for line in symbols:
	line = line.replace('\n', '')
	pair = line.split ('\t')
	ge = pair [0]
	ipa = pair [1]
	if ge not in table:
		table [ge] = ipa
```
We read input file line by line, output original sentence, then split it into words, and in every word we check if the symbol maps the key from dictionary with transliteration table. If so, we form new word, add it to new line, and print it to output.
```
ge_text = sys.stdin.read()
ge_text = ge_text.replace ('. ', '.\n')
ge_text = ge_text.split ('\n')

for line in ge_text:
	if line not in ' ':
		print ('Original sentence: ', line)
		ipa_line = 'IPA: '
		words = line.split()
		for w in words:
			ipa_w = ''
			for smb in w:
				if smb in table:
					ipa_smb = table[smb]
				else:
					ipa_smb = smb
				ipa_w = ipa_w + ipa_smb
			ipa_w = ipa_w + ' '
			ipa_line = ipa_line + ipa_w
		print (ipa_line, '\n')
```
To test the script, we have prepared file `ge_wiki.txt`. It is used as an input like this:
```
cat ge_wiki.txt | python3 ge_transliterate.py
```
The output of the script looks like:
```
ADD EXAMPLE HERE
```

#### EVALUATION
problems...
