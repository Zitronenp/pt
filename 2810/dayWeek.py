import datetime


def gendates(year, month, day):
    date = datetime.datetime(year, month, day)
    while True:
        yield date.strftime("%d %m %Y %A")
        date += datetime.timedelta(days=1)

year, month, day = map(int, input().split())
f = gendates(year, month, day)
for i in range(int(input())):
    print(next(f))