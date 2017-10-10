file = open('Kaartnummers.txt', 'r')
content = file.readlines()
file.close()
for line in content:
    args = line.split(',')
    args[1] = args[1].rstrip('\r\n')
    print(args[1] + ' heeft kaartnummer: ' + str(args[0]))