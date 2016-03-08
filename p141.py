import re
sum = 0
count = 0
hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('New Revision: ([0-9]+)', line)
    if len(x) > 0:
        for item in x:
            num = float(item)
            sum = sum + num
            count = count + 1
print (sum/count)
