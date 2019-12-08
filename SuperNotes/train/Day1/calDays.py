import datetime

"""
计算两个日期之间的天数（日期格式如“1970-01-01”）
"""

def calDays(date_one: str, date_two: str) -> int:
    if '-' in date_one and '-' in date_two:

        date_one_tup = tuple(int(n) for n in date_one.split('-'))
        d1 = datetime.datetime(year=date_one_tup[0], month=date_one_tup[1], day=date_one_tup[2])

        date_two_tup = tuple(int(n) for n in date_two.split('-'))
        d2 = datetime.datetime(year=date_two_tup[0], month=date_two_tup[1], day=date_two_tup[2])

        between_days = (d1 - d2).days
        print('日期【{}】和【{}】之间相隔{}天。'.format(date_one, date_two, between_days))
        return between_days
    else:
        print('日期格式不合法，请重新输入格式如“1970-01-01”的日期！')
        return 0

if __name__ == '__main__':
    date_first = input('请输入第1个日期，格式如“1970-01-01”')
    date_second = input('请输入第2个日期，格式如“1970-01-01”')
    calDays(date_first, date_second)
