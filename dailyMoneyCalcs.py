import datetime

def calcDiff():
    currentDate = datetime.date.today()

    month = currentDate.month
    # inc the month by 1 if the payday for this month has already past
    month += 0 if currentDate.day < 15 else 0
    # if the payday month has gone to 13 (e.g. if december payday has passed
    # ) change the month to January
    month = 1 if month == 13 else month

    payday = datetime.date(2020,month,15)
    weekday = payday.weekday()

    if (weekday == 5):
        payday.day -= 1
    elif (weekday == 6):
        payday.day -= 2

    diff = (payday - currentDate).days

    return diff, payday

def calcDaily(bankaccount, save, diff):
    return "£" + str(round((bankaccount-save)/diff,2))