age = eval(input('Geef je leeftijd: '))

hits = 10
shield = 0
if age > 62:
    print('You can get Social Security benefits')

report = input('give a string:')
if 'large bonuses' in report.lower():
    print('Vacation time!')

if hits >= 10 and shield == 0:
    print('you are dead')
else:
    print('staying alive')