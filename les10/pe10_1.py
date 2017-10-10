import xmltodict

with open('magazijn.xml') as mz:
    content = xmltodict.parse(mz.read())

# print(content)

for item in content['artikelen']['artikel']:
    print('{} {} {} {} {}'.format(item['@nummer'],item['code'],item['naam'],item['voorraad'],item['prijs']))