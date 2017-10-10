def ticker(filename):
    ticker = {}
    file = open(filename,'r')
    lines = file.readlines()
    file.close()
    for line in lines:
        splitline = line.split(':')
        splitline[1] = splitline[1].strip('\n')
        ticker[splitline[0]] = splitline[1]
    return ticker


ticker = ticker('tickers.txt')
tickerinput = input('Enter Ticker name: ')
if tickerinput in ticker.values():
    for(company, ticker) in ticker.items():
        if ticker == tickerinput:
            print(company)

companyinput = input('Enter Company name: ')
if companyinput in ticker:
    print(ticker[tickerinput])
