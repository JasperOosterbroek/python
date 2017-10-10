students = {'Jasper': 10.0,
             'Kees' : 6.0,
             'Piet' : 8.7,
             'Sjaak' : 8.0,
             'Jan': 3.6,
             'Jaap' : 7.3,
             'Gerard' : 9.7,
             'Mike' : 7.7,
             'Tim' : 3.6,
             'Guus' : 9.5
            }
for (naam, cijfer) in students.items():
    if cijfer >= 9.0:
        print('{} heeft een {} behaald'.format(naam,cijfer))