import urllib
import json

while True:
    url = raw_input('Enter url: ')
    if len(url) < 1 : break
    
    html = urllib.urlopen(url).read()
    print 'Retrieved', len(html), 'characters'

    info = json.loads(html)
            
    count = 0
    sum = 0

    while True:
        num = info["comments"][count]["count"]
        print count
        print "count:", num
        count = count + 1
        
        sum = sum + num
        print "sum:", sum