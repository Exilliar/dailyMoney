from tkinter import *
from functools import partial

from dailyMoneyCalcs import calcDaily


def gui(diff, payday):
    def calc_result(output, inp, save_label):
        try:
            save = float(save_label.get()) if (save_label.get() != "") else 500
            money = float(inp.get())
            daily = calcDaily(money, save, diff)
            output.config(text=daily)
        except Exception as e:
            print("e:", e)
            output.config(text='Error')

    master = Tk()

    master.title("Daily Money")

    Label(master, text='Next payday ' + str(payday)).grid(row=0)
    Label(master, text='Days left ' + str(diff)).grid(row=0, column=1)

    Label(master, text='Bank account').grid(row=1)

    inp = Entry(master)
    inp.grid(row=1, column=1)

    Label(master, text='Money to save (assumes 500)').grid(row=2)
    save_label = Entry(master)
    save_label.grid(row=2, column=1)

    Label(master, text='Spend per day:').grid(row=4)
    output = Label(master)
    output.grid(row=4, column=1)

    calc_result = partial(calc_result, output, inp, save_label)

    button = Button(master, text='Calculate', width=25,
                    command=calc_result).grid(row=3, columnspan=2)

    mainloop()
