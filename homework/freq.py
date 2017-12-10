import sys

vocab = {} # dict to store frequency list

# a loop where value for key 'form' will be encreased on every step if the form is already in the dict 

# for each of the lines of input
for line in sys.stdin.readlines(): 
	# if there is no tab character, skip the line
	if '\t' not in line:
		continue
	# make a list of the cells in the row
	row = line.split('\t')
	# if there are not 10 cells, skip the line
	if len(row) != 10:
		continue
	# the form is the value of the second cell
	form = row[1].strip() # this function must remove everything before and after every word, but it doesn't !!!
	# if we haven't seen it yet, set the frequency count to 0
	if form not in vocab:
		vocab[form] = 0 #записываем в словарь key и value
	vocab[form] = vocab[form] + 1 # увеличиваем value

# dictionary is not sortable, and our results are kept in random order, so we:

# create list to print frequency in freq order since list is a sortable datastructure
freq = [] #a list of value:key tuples - это список кортежей, каждый кортеж - наша пара из словаря
for w in vocab: # для каждого элемента (назовем любым образом) в нашем словаре
	freq.append((vocab[w], w)) # добавим в список кортеж, который состоит из значения для ключа и самого ключа

freq.sort(reverse=True) # отсортируем по убыванию

# print first and second element from every tuple with tab between them
for i in freq:
	print (i[0], i[1], sep = '\t')

