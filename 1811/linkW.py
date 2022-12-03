import urllib

import lxml.html
connection = urllib.urlopen('https://ru.wikipedia.org/wiki/Сыр#:~:text=Сыр%20—%20пищевой%20продукт%20в,метатезного%20характера%20праслав.%20*surowatъka)%2C%20суровый')

dom =  lxml.html.fromstring(connection.read())

for link in dom.xpath('//a/@href'): # select the url in href for all a tags(links)
    print(link)
