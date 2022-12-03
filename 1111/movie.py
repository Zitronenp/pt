from lxml import etree as ET
tree = ET.parse('movies.xml')
root = tree.getroot()