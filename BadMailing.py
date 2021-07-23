
import re
import numpy as np
count=0
name = list()
address = list()
city = list()
Maddress = list()

fh = fh = open('BadMailing.txt')
for lines in fh:
    line = lines.rstrip()
    parish = re.findall('(\:.*\s\(.*\))\s\.*', lines)
    # parish = re.findall('(.*?)', lines)
    if lines.startswith('NEW') or lines.startswith('BLESSED SACRAMENT (III C) (773) 523-3917') or len(lines) < 4:
        # print(lines)
        continue
    if lines.startswith('SHRINES, CHAPLAINCIES, AND ORATORIES') or lines.startswith('MISSIONS'):
        break

    if lines.startswith('PARISHES') or lines.startswith( 'MISSIONS') or lines.startswith('BLESSED SACRAMENT (III C) (773) 523-3917') or len(lines) < 4:
        # print(lines)
        continue

    if len(parish) >0:
        name.append(parish)
        print('PARISH: ', parish)

    # if lines.startswith('RECTORY:') or lines.startswith('CHURCH:'):
    #     if len(name)== len(address):
    #         continue
    #     else:
    #         address.append(line)
    #         print('ADDRESS:', line)
    #         # print(address)


    if lines.startswith('MAILING ADDRESS: '):
        mail = re.findall('MAILING ADDRESS:\s(.*)', lines)
        Maddress.append(line)
        print('MAIL: ', mail)
print(len(name), len(Maddress), len(address))


for i in range(len(name)):
    print(name[i], ';', Maddress[i])

print(len(name), len(Maddress))

#
# BLESSED SACRAMENT (III C) (773) 523-3917
# RECTORY: 3745 S. Paulina St., Chicago, IL 60609-2047 Fax: (773) 247-9285
# SS. PETER AND PAUL SITE: 3745 S. Paulina St., Chicago, IL 60609
# OUR LADY OF GOOD COUNSEL SITE: 3528 S. Hermitage Ave., Chicago, IL 60609
# ST. MAURICE SITE: 3615 S. Hoyne Ave., Chicago, IL 60609
# EMAIL: blessedsacrament@archchicago.org
# PASTOR: Rev. Ismael Sandoval
# ASSOCIATE PASTOR: Rev. Cristian R. Cuevas Jara, SCJ
# DEACON(S): Juan M. Rosales, Dismas Fernandez
