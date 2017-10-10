import random
def monopolyworp():
    jailroll = 0
    d1= random.randrange(1,7)
    d2= random.randrange(1,7)
    while d1 == d2:
        print('{} + {} = {} (dubbel)'.format(d1,d2,d1+d2))
        jailroll += 1
        d1 = random.randrange(1, 7)
        d2 = random.randrange(1, 7)
        if jailroll >= 3:
            print('{} + {} = {} (Direct naar de gevangenis)'.format(d1, d2, d1 + d2))
            break
    print('{} + {} = {}'.format(d1, d2, d1 + d2))


monopolyworp()
