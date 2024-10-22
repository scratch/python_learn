# Display all the words occuring in a input file, sorted.
#
# 8.4 Open the file romeo.txt and read it line by line. For each line,
# split the line into a list of words using the split() method. The
# program should build a list of words. For each word on each line
# check to see if the word is already in the list and if not append it
# to the list. When the program completes, sort and print the resulting
# words in alphabetical order.
#
#You can download the sample data at http://www.pythonlearn.com/code/romeo.txt

lwords = list()
allwords = list()

fname = raw_input("Enter file name: ")
fh = open(fname)

for line in fh:
    lwords = line.split()
    for lword in lwords:
        if not lword in allwords:                   
            allwords.append(lword)
            

allwords.sort()
print allwords
