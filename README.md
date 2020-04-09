# DailyMoney

Python script for basic daily money management

# Usage

## Once built (see below for instructions)

dailMoney  
dailyMoney -g

## Before building
python3 \_\_main\_\_.py  
python3 \_\_main\_\_.py -g

### Options:  
-g&nbsp;&nbsp;-gui  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Runs the program using a GUI rather than the default terminal interface

# Notes

1. Uses python3

2. Both the GUI and terminal interfaces require the same info from the user

3. The program assumes that payday is on the 15th of each month. If that day falls on the weekend then it changes to the Friday before

# Flow

1. The program will ask for the total amount of money that the user has

2. It will then ask how much the user wishes to save by their payday (defaults to £500)

3. It will output the total amount that can be spent per day until payday

# Building

To build on ubuntu (and probably other unix machines) run commands

1. `mkdir build`
2. `zip -r build/dailyMoney.zip *`
3. `cd build/`
4. `echo '#!/usr/bin/env python3' | cat - dailyMoney.zip > dailyMoney`
5. `chmod -x dailyMoney`

Check that it's now working run `./dailyMoney`. It should fully work

There is also the bash script `createBuild.bash` that can be run. It follows the instructions above, however uses `chmod 777 dailyMoney` as the final command for reliability

## Make command available on ubuntu

To make the `dailyMoney` command available for use anywhere on linux, copy the `dailyMoney` executable created in the  previous section into `/bin`. It should then work fully

### If anything goes wrong

Check http://blog.ablepear.com/2012/10/bundling-python-files-into-stand-alone.html for instructions on how to build python scripts into an executable