import urllib
import re

#print dir(urllib)

url = 'http://www.py4inf.com/book.htm'
fp = urllib.urlopen(url)
html = fp.read()
print html
print '------------'
links = re.findall('href="(http://.*?)"', html)
#links = re.findall('href="(http://.*)"', html)

for link in links:
    print link
