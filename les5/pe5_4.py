def strftime():
    import datetime
    vandaag = datetime.datetime.today()
    s = vandaag.strftime("%a %d %b %Y %H:%M:%S")
    return s

file = open('hardlopers.txt', 'a')
name = input('Voer een of meerdere namen in gescheiden met een comma: ')
nameList = name.split(',')
for name in nameList:
    file.write(strftime()+', '+ name.strip()+'\n')