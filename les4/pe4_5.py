def kwadraten_som(numbers):
    sqrtvalue = 0
    for square in numbers:
        if square >= 0:
            sqrtvalue += square**2
    return sqrtvalue

print(kwadraten_som([4,5,3,-81]))