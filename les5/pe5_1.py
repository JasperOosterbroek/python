def convert(temprature):
    return temprature * 1.8 + 32

def table():
    print('  {0:^4}{1:^12}'.format('F', 'C'))
    for i in range(-30, 50, 10):
        print('{0:^8}{1:^8}'.format(convert(i),float(i)))

table()