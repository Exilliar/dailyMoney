from dailyMoneyCalcs import calcDaily


def terminal(diff):
    bankaccount = float(input("How much money left: "))
    save = input("How much money to put in savings (500): ")
    save = 500.0 if save == "" else float(save)

    daily = calcDaily(bankaccount, save, diff)

    print("daily: " + daily)
