import sys

#create counters for liness, words and characters
counter_lines = 0
counter_tokens = 0
counter_char = 0

#create empty string 
text = ''

#read from our corpus
for line in sys.stdin.readlines():
	text += line

#all letters small

text = text.lower()

# number of lines is a number of \n,
# number of words is a number of spaces,
# number of chatacters - from the list of all turkish char-s
for a in text:
	if a == '\n': 
		counter_lines += 1
	if a == " ":
		counter_tokens = counter_tokens+1
	if a in 'abcçdefgğhiıjklmnoöprsştuüvyz':
		counter_char = counter_char+1

print ("Number of lines: ", counter_lines)
print ("Number of tokens: ", counter_tokens)
print ("Number of characters: ", counter_char)
