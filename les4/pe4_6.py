def wijzig(letterlijst):
    letterlijst[:] = ['d','e','f']

letterlijst = ['a','b','c']
wijzig(letterlijst)
print(letterlijst)
#  omdat je dan buiten je eigen scope probeert te werken
# nee omdat strings immutable zijn
# immutablititie speelt een hele grote rol