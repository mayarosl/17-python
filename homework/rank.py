import sys
# new list to keep frequency again?
freq = []

# open our frequency list stored in the file
fd = open('freq.txt', 'r')
for line in fd.readlines():
	line = line.strip('\n') #create line variable
	(f, w) = line.split('\t') # tuples of frequency and word form
	freq.append((int(f), w))

rank = 1
min = freq[0][0] 
ranks = [] # new list to keep rank + freq value + key
for i in range(0, len(freq)): # для элемента в диапазоне между 0 и числом, равным длине списка freq
	if freq[i][0] < min: # если первый элемент первого кортежа меньше min
		rank = rank + 1 # увеличиваем индекс
		min = freq[i][0] # записываем новое значение в переменную
	ranks.append((rank, freq[i][0], freq[i][1])) # добавляем в список индекс, первый елемент кортежа и второй элемент кортежа

for a in ranks:
	print (a[0], a[1], a[2], sep = '\t')
