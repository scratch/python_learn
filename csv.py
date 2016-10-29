import re
import csv

print dir(csv)
with open('/tmp/sales.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print row
