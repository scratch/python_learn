import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
if (len(url) < 1): 
    url = 'http://python-data.dr-chuck.net/known_by_Fikret.html'
    #url = 'http://python-data.dr-chuck.net/known_by_Elle.html'

#position = raw_input('Enter position')
#count = raw_input('Enter Count')
position = 3
count = 4
#position = 18
#count = 7


while count > 0:
    # cur_pos = position  -- only required for for loop, but can get 
    # link directly from lnks[] list!
    count = count - 1
    print url

    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    lnks = soup('a')

    # TODO: Change the for to: 
    # get url = lnks[position].get('href', None
    #for lnk in lnks:
    #    url = lnk.get('href', None)
    #    cur_pos = cur_pos - 1
    #    if cur_pos == 0:
    #        break

    url = lnks[position-1].get('href', None)

print url


