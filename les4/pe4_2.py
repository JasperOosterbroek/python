def som(somlist):
    if type(somlist) == list:
        return sum(somlist)
    else:
        return 'de meegegeven waarde is geen lijst'

numberlist = [2,4,6]
print(som(numberlist))