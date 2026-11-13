import xml.dom.minidom as minidom


xml_file = open('currency.xml', 'r')
xml_data = xml_file.read()

dom = minidom.parseString(xml_data)
dom.normalize()

elements = dom.getElementsByTagName('Valute')
books_dict = {}
charcode = []
value = []

for node in elements:
    charcode.append(node.getElementsByTagName("CharCode")[0].firstChild.data)
    value.append(node.getElementsByTagName("Value")[0].firstChild.data)
print(charcode)
print(value)


xml_file.close()
