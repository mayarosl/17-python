## From Georgian script to IPA

Georgian is one of Kartvelian languages, a language family indigenous to the Caucasus. Georgian is written in its own writing system, the Georgian script. The modern Georgian script, *Mkhedruli*, has been in use since the 11th century. There are 28 phonemic consonants in Standard Georgian, and 5 vowels[1].

IPA is an abbreviation for [The International Phonetic Alphabet](www.internationalphoneticassociation.org). It is an alphabetic system of phonetic notation aimed to illustrate a standardized representation of the sounds of spoken language.

OFFICIAL SOURCE??? LINK

### Propject

***First step*** is a table of Georgian → IPA symbols mapping. The file is two columns, separated by a tab \t character.
A table looks simplistic due to several points. First, there are no capital letters in Georgian. Second, there is a one-to-one correspondence between the alphabetic symbols and phonemic sounds. 

It looks like:
```
        ა	ɑ
        ბ	b
        გ	g
        ...
```

The table is stored in `ge_table.txt`.

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
