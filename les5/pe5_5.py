def gemiddelde(sentence):
    words = sentence.split()
    average = sum(len(word) for word in words) / len(words)
    return int(average)

sentence = input('Vul een zin in: ')
print('gemiddelde woord lengte is {}'.format(gemiddelde(sentence)))