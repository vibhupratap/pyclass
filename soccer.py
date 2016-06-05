


file_open = open('soccer.txt','r')
count = 0
for line in file_open:
    if line.split(',')[3] == 'GK':
        count = count + 1

print count
