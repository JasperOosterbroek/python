def lang_genoeg(length):
    if length >= 120:
        return 'Je bent lang genoeg voor de attractie!'
    else:
        return 'Sorry, je bent te klein!'

length = eval(input('Wat is je lengte in centimeter? '))
print(lang_genoeg(length))