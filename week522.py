import urllib
import xml.etree.ElementTree as ET

sum = 0

while True:
    url = raw_input('Enter url: ')
    if len(url) < 1 : break
    
    html = urllib.urlopen(url).read()
    tree = ET.fromstring(html)
    count = tree.findall('comments/comment')

    for item in count:
        num = item.find('count').text
        inum = int(num)
        sum = sum + inum
    print sum