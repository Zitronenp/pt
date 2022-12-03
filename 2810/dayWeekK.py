import datetime


def gendates(date):
    while True:
        yield date.strftime("%d %m %Y")
        date += datetime.timedelta(days=1)


def gendow(date):
    while True:
        yield date.strftime("%A")
        date += datetime.timedelta(days=1)


def genall(date):
    while True:
        an= next(gendates(date))+' '+next(gendow(date))
        yield an
        date += datetime.timedelta(days=1)


year, month, day = map(int, input().split())
date = datetime.datetime(year, month, day)
f = genall(date)
for i in range(int(input())):
    print(next(f))
