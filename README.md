# DailyMoney

Python script for basic daily money management

# Usage

python3 dailMoney.py  
python3 dailyMoney.py -g

Options:  
-g&nbsp;&nbsp;-gui  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Runs the program using a GUI rather than the default terminal interface

# Notes

1. Uses python3

2. Both the GUI and terminal interfaces require the same info from the user

3. The program assumes that payday is on the 15th of each month. If that day falls on the weekend then it changes to the Friday before

# Flow

1. The program will ask for the total amount of money that the user has

2. It will then ask how much the user wishes to save by their payday (defaults to £500)

3. It will output the total amount that can be spent per day until payday