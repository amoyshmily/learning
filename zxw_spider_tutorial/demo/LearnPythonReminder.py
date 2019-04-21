
receivers = ['敏达', '易利', '陈静', '尹清', '光叔']


def remind(name):

    week = {}
    week['Monday'] = 'learn python'
    week['Tuesday'] = 'learn python'
    week['Wednesday'] = 'learn python'
    week['Thursday'] = 'learn python'
    week['Friday'] = 'learn python'
    week['Saturday'] = 'learn python'
    week['Sunday'] = 'learn python'

    for day in week.keys():
        words = '{} should {} on {}'.format(name, week[day], day)
        print(words)


if __name__ == '__main__':
    for year in range(2019, 9999):
        for receiver in receivers:
            remind(receiver)
