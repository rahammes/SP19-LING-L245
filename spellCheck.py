fd = open('wiki.hist', 'r')
hist = fd.read()
hist1 = hist.split()

input = str(input("Enter a phrase: "))
input1 = input.split()
for words in input1:
	if words in hist1:
		print(words, end = ' ')
	else:
		print(words+'*', end = ' ')
print()