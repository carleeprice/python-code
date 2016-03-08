import urllib
from BeautifulSoup import *

topcount = 0

url = raw_input('Enter - ')
while topcount <= 6:
    subcount = 0
    print "Opening:", url
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    for tag in tags:
        link = tag.get('href', None)
        print topcount, subcount, link
        subcount = subcount + 1
        if (subcount >= 18):
            break
    url = link
    topcount = topcount + 1
print url