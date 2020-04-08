# Libraries for getting options
import sys
import getopt

from dailyMoneyCalcs import calcDiff

# Two different ways the program can take inputs/outputs
from dailyMoneyTerminal import terminal
from dailyMoneyGUI import gui

try:
    opt, args = getopt.getopt(sys.argv[1:],"g",["gui"])
except getopt.GetoptError:
    print("option not recognised")

diff, payday = calcDiff()

if (len(opt) == 0):
    terminal(diff)
elif (opt[0][0] == "-g" or opt[0][0] == "--gui"):
    gui(diff, payday)