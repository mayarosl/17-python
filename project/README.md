## From Georgian script to IPA

#### INTRO

IPA is an abbreviation for [The International Phonetic Alphabet](https://www.internationalphoneticassociation.org/). It is an alphabetic system of phonetic notation aimed to illustrate a standardized representation of the sounds of spoken language.

Georgian is one of Kartvelian languages, a language family indigenous to the Caucasus. Georgian is written in its own writing system, the Georgian script. The modern Georgian script, *Mkhedruli*, has been in use since the 11th century. There are 28 phonemic consonants in Standard Georgian, and 5 vowels. Wovels are: i, &#603;, &#593;, o, u. Here is a chart of Georgian consonants from Shosted & Chikovani (2006):

<img src="https://4.downloader.disk.yandex.ru/disk/6467c97a6b749664959339b0a0a6632d48065f0204a07d7637539f3903943ac3/5a374936/U6tpeiIpRI7Zg034NSXqvuNGfnz4gBt5eCAKJfI7Q-qtSIVeZQS3Pv1UQGnKgfrV4Pc0LLXKKwIGU3AtkNQJAQ%3D%3D?uid=0&filename=2017-12-18_03-49-27.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&fsize=42097&hid=7b61ce6b64dc38e9d1d3c5bf0f6d9ad3&media_type=image&tknv=v2&etag=a150d6374993e593b80713768f840357" width="600">

Georgian is well known for its complex morphology, but not much is known about its intonation. The language is claimed to have stress, although its exact realization is debated in the literature. Additionaly, it is not fixed. Thus, it is not seen as possible to mark stress in the IPA transcription.

#### PURPOSE
The program is aimed to take a text in Georgian language from input, split words into morphems and transfer it into IPA symbols. We are going to transcribe phonemically. The output will represent not actual sounds, but abstract mental constructs, i.e. the categories of sound that speakers understand to be ‘sounds of their language’. 

#### PROJECT DESCRIPTION
The project consists of a transliteration table, a table of morphems and a script itself.

***First step*** is a table of Georgian → IPA symbols mapping. The file consists of two columns separated by a tab `\t` character.
The table looks simplistic due to several points. First, modern Georgian alphabet is caseless. Second, there is a one-to-one correspondence between the alphabetic symbols and phonemic sounds. 

The table looks like:
```python 
	ა	ɑ
	ბ	b
	გ	g
	... 
```
... and it is stored in `ge_table.txt`.

***Second step*** is a table of Georgian morphems. Like in the first step, it is a text file with two columns separated by a tab `\t`. Only first column is needed for script, second one is just for comments:
```python
	ი	NOM
	მა	ERG
	ს	DAT

```
The table is stor
PROMLEM: I don't know GE and don't have time to check all of them.


***Third step*** is a code itself. Python reads the `ge_table.txt` and form the dictionary of Georgian → IPA symbols mapping.
```python
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
The input file with text in Georgian is read line by line. Python outputs original sentence, then splits it into words, and in every word checks if the symbol maps the key from dictionary with transliteration table. If so, it forms the new word, adds it to a new line, and prints it to output.
```python
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
To test the script, I have prepared file `ge_wiki.txt`. It is used as an input like this:
```
$ cat ge_wiki.txt | python3 ge_transliterate.py ge_table.txt
```
The output of the script looks like:
```html
Original sentence:  ჩემი გამოცდილების მიხედვით, ებრაელები არ არიან ხალხთა სხვა ჯგუფებზე უკეთესნი, თუმცა, ყველაზე ცუდი სიმსივნური ელემენტებისგან მათ ხელისუფლების არყოლა იცავს.
IPA: tʃʰɛmi gɑmɔtsʰdilɛbis miχɛdvitʰ, ɛbrɑɛlɛbi ɑr ɑriɑn χɑlχtʰɑ sχvɑ dʒgupʰɛbzɛ ukʼɛtʰɛsni, tʰumtsʰɑ, qʼvɛlɑzɛ tsʰudi simsivnuri ɛlɛmɛntʼɛbisgɑn mɑtʰ χɛlisupʰlɛbis ɑrqʼɔlɑ itsʰɑvs.
```

#### EVALUATION

:+1: The script works properly. It can be adjusted to output a plain text (without original sentences) or a list of words in IPA.

:-1: Due to the flexible stress in Georgian, forms in IPA are not marked with stress.

:-1: The script works only with Georgian alphabet, any symbol from another system (if it is in an input text) will not be transfered into IPA. At least latin and cyrillic symbols should be added to the table with mappings.


***** 

Shosted, R., & Chikovani, V. (2006). Standard Georgian. Journal of the International Phonetic Association, 36(2), 255-264. doi:10.1017/S0025100306002659, [PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/A7DCF9606BA856FCA5CC25918ADB37EF/S0025100306002659a.pdf/standard_georgian.pdf)



Добавила:
прога отделяет падежные окончания существительных
проблемы:
в тексте не видно, что есть сущ
я не знаю грамматику так хорошо, может есть совпадения с другими чр
лучше будет работать, если применить в токенизированному тексту и задать параметр НАУН
то есть как я могу улучшить проектЖ
аннотировать кусок текста
применять разные таблицы окончаний к разным частям речи
