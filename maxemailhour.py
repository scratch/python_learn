#10.2 Write a program to read through the mbox-short.txt and figure
#out the distribution by hour of the day for each of the messages. You
#can pull the hour out from the 'From ' line by finding the time and
#then splitting the string a second time using a colon.
#
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)

lwords = list()
hrcnt = dict()
for line in fh:
    if line.startswith('From') and not  line.startswith('From:'):
        lwords = line.split()
        fulltime = lwords[5]
        hr = fulltime [ : lwords[5].find(':')]
        hrcnt[hr] = hrcnt.get(hr, 0) + 1

hrout = hrcnt.items()
hrout.sort()
for key, val in hrout:
    print key, val

