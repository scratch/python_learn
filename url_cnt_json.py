import json
import urllib

address = raw_input('Enter location: ')
if len(address) < 1:
    #address = 'http://python-data.dr-chuck.net/comments_42.json'
    address = 'http://python-data.dr-chuck.net/comments_316255.json'

print 'Retrieving', address
data = urllib.urlopen(address).read()
print 'Retrieved', str(len(data)), 'characters'

json_data = json.loads(data)
#print json.dumps(json_data, indent=4)
count = 0
for item  in json_data['comments']:
    count = count + int(item['count'])

print 'count:', count



