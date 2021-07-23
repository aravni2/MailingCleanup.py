
import re
import numpy as np
count=0
name = list()
street = list()
address = list()
city = list()
Maddress = list()
state = list()

with open("BadMailing.txt", "r") as orig:
    lines = orig.readlines()
with open("BadMailing2.txt", "w") as f:
    for line in lines:
        line = line.rstrip()
        if line.startswith('USPS') or line.startswith('Date') or line.startswith('Domestic') or line.startswith('Prepared'):
            continue
        else:
            f.write(line + '\n')
with open('BadMailing2.txt', 'r') as orig:
    lines = orig.readlines()
    for line in lines:
        print(line)


fh = open('BadMailing2.txt')
for lines in fh:
    line = lines.rstrip('\n')
    line = lines.lstrip(('NEW Address:'))
    stuff = re.findall('\S+', line)
    # print(line)
    count += 1
    if count%2.0 == 0:
        street.append(line)
        # print(line, count)
    elif count%3.0 == 0:
        splits = line.split(', ')
        # splits = splits.strip()
        # print(splits)
        city.append(splits[0])
        state.append(splits[1])
        # print(line, count)
        count = count -3
    else:
        name.append(line)
        print(line, count)


print(name, len(name))
print(street, len(street))
print(city, len(city))
print(state, len(state))
# #
print(len(name))
print(len(street))
print(len(city))
print(len(state))

mlist = [name, street, city, state]
print(mlist)


for i in range(len(name)):
    count = count+1
    print(name[i].strip(),":",street[i].strip(),":",city[i].strip(),":", state[i].strip(), count)