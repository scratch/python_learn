# Test Program
import re

s = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
str = re.findall('@(\S+)', s)
str2 = re.findall('@(\S+) .+$', s)
str3 = re.findall('@(\S+?)', s)   

x = 'From: Using the : character'
y2 = re.findall('^F.+:?', x)
y = re.findall('^F.+:', x)

print 'y: ', y
print 'y2 using ?: ', y2
print 'str: ', str
print 'str2', str2
print 'str3', str3

s2 = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
str = re.findall('\S+?@\S+', s2)
print "New Str", str

s3 = '<p>Please click <a href="http://www.dr-chuck.com">here</a></p'
str = re.findall('http://.*', s3)
print str

str = re.findall('href="(.+)"', s3)
print str
