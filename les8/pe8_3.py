def code(invoerstring):
    sentence = ''
    for letter in invoerstring:
        char = chr(ord(letter)+3)
        sentence += char
    return sentence

print(code('Pannekoeken'))