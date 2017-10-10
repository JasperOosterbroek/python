def stadaardprijs(afstandKM):
    if afstandKM >= 50:
        return afstandKM * 0.6 + 15
    else:
        if afstandKM  > 0:
            return afstandKM * 0.8
        else:
            return 0


def ritprijs(leeftijd, weekendrit, afstandKM):
    stprice = stadaardprijs(afstandKM)
    if weekendrit == True:
        if leeftijd < 12 or leeftijd  >= 65:
            return stprice * 0.60
        else:
            return stprice * 0.65

    else:
        if leeftijd < 12 or leeftijd  >= 65:
            return stprice
        else:
            return stprice * 0.70



print(ritprijs(11, True, -1)) #0
print(ritprijs(12, True, -1)) #0
print(ritprijs(64, True, -1)) #0
print(ritprijs(65, True, -1)) #0

print(ritprijs(11, False, -1)) #0
print(ritprijs(12, False, -1)) #0
print(ritprijs(64, False, -1)) #0
print(ritprijs(65, False, -1)) #0

print(ritprijs(11, True, 25)) # 12
print(ritprijs(12, True, 25)) # 13
print(ritprijs(64, True, 25)) # 13
print(ritprijs(65, True, 25)) # 12

print(ritprijs(11, False, 25)) #0
print(ritprijs(12, False, 25)) #0
print(ritprijs(64, False, 25)) #0
print(ritprijs(65, False, 25)) #0


print(ritprijs(11, True, 55)) #0
print(ritprijs(12, True, 55)) #0
print(ritprijs(64, True, 55)) #0
print(ritprijs(65, True, 55)) #0

print(ritprijs(11, False, 55)) #0
print(ritprijs(12, False, 55)) #0
print(ritprijs(64, False, 55)) #0
print(ritprijs(65, False, 55)) #0