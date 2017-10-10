def devide(amount):
    try:
        if amount < 0:
            return 'Negatieve getallen zijn niet toegestaan!'
        moneyPerPerson = 4356 / amount
        return round(moneyPerPerson, 2)
    except TypeError:
        return 'Gebruik cijfers voor het invoeren van het aantal'
    except ZeroDivisionError:
        return 'Delen door 0 kan niet!'
    except:
        return 'Onjuiste invoer'

print(devide(0))
print(devide(-20))
print(devide('twintig'))
print(devide(1234))


