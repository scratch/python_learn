# sum up all the number in file

#The basic outline of this problem is to read the file, look for
#integers using the re.findall(), looking for a regular expression of
#'[0-9]+' and then converting the extracted strings to integers and
#summing up the integers.

import re

name = raw_input("Enter file:")
if len(name) < 1 : name = "sample-data.txt"
fh = open(name)

numlist = list()

for line in fh:
    numlist = numlist + re.findall('[0-9]+', line)

totSum = 0

for i in numlist:
    totSum = totSum + int(i)

print totSum
