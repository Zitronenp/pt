import datetime

import ds3 as ds3


def gendates(year, month, day):
    date = datetime.datetime(year, month, day)
    while True:
        yield date
        date += datetime.timedelta(days=1)


year, month, day = input().split()
year, month, day = [int(year), int(month), int(day)]
#year, month, day = map(int, input().split())
#dt3 = datetime.strptime(ds3, '%m-%d-%Y')
f = gendates(year, month, day)
for i in range(int(input())):
    print(next(f))
