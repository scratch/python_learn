import urllib
import xml.etree.ElementTree as ET

address = raw_input('Enter location: ')
if len(address) < 1:
    #address  = 'http://python-data.dr-chuck.net/comments_42.xml'
    address = 'http://python-data.dr-chuck.net/comments_316251.xml'

data = urllib.urlopen(address).read()
tree = ET.fromstring(data)
cmt_list = tree.findall('comments/comment')

tot_sum = 0
lines = 0
for cmt in cmt_list:
    tot_sum = tot_sum + int(cmt.find('count').text)
    lines = lines + 1

print 'Retrieving '  + address
print 'Retrieved '  + str(len(data)) + ' characters'
print 'count '  + str(lines)
print 'Sum '  + str(tot_sum)

