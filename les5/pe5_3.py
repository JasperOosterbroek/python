file = open('Kaartnummers.txt', 'r')
content = file.readlines()
file.close()
lineAmmount = len(content)
highestNumberIndex = content.index(max(content))
tmpHighestNumber = content[highestNumberIndex].split(',')
highestNumber = tmpHighestNumber[0]

print('Deze file telt ' + str(lineAmmount) + ' regels\nHet grootste kaartnummer is: '+ str(highestNumber)+' en dat staat op regel ' + str(highestNumberIndex+1))