def namen():
    namen= {}
    naam = input('Volgende naam: ')
    while (len(naam) != 0):

        if not naam in namen:
            namen[naam] = 1
        else:
            namen[naam] += 1

        naam = input('Volgende naam: ')
    for (key, value) in namen.items():
        if value == 1:
            print('er is {} student met de naam {}'.format(value,key))
        else:
            print('Er zijn {} studenten met de naam {}'.format(value,key))


namen()
