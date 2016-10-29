#Scraping Numbers from HTML using BeautifulSoup In this
#assignment you will write a Python program similar to
#http://www.pythonlearn.com/code/urllink2.py. The program will use
#urllib to read the HTML from the data files below, and parse the data,
#extracting numbers and compute the sum of the numbers in the file.

#We provide two files for this assignment. One is a sample file where
#we give you the sum for your testing and the other is the actual data
#you need to process for the assignment.

#Sample data: http://python-data.dr-chuck.net/comments_42.html (Sum=2553)
#Actual data: http://python-data.dr-chuck.net/comments_316254.html (Sum ends with 19)

#        You do not need to save these files to your folder since
#your program will read the data directly from the URL. Note: Each
#student will have a distinct data url for the assignment - so only
#use your own data url for analysis.


# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter URL - ')
if (len(url) < 1):
    #url = "comments_42.html"
    url = 'http://python-data.dr-chuck.net/comments_316254.html'

html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
# Retrieve all of the anchor tags
tags = soup('span')

content_sum = 0
content_cnt = 0
# Other useful BeautifulSoup stuff.
    #print 'TAG:',tag
    #print 'URL:',tag.get('href', None)
    #print 'Contents:',tag.contents[0]
    #print 'Attrs:',tag.attrs
#
for tag in tags:
    content_sum = content_sum + int(tag.contents[0])
    content_cnt = content_cnt + 1

print 'Count',content_cnt
print 'Sum',content_sum
