count = 0
dic = dict()
fname = raw_input("Enter file:")
if len(fname) < 1: fname = "mbox-short.txt"
fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    if line == '':
        continue
    word = line.split()
    if word[0]=='From:':
        continue
    if word[0]!='From':
        continue
    time = word[5]
    hour, min, sec = time.split(':')
    if hour not in dic:
        dic[hour] = 1
    else: 
        dic[hour] = dic[hour] + 1
list = dic.items()
list.sort()
for hour,count in list:
    print hour, count