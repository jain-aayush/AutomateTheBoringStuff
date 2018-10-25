"""
Write a program that tracks the amount of time elapsed between presses of the ENTER key, 
with each key press starting a new “lap” on the timer.
Print the lap number, total time, and lap time in a prettified format.
Also, copy the output to clipboard.
"""

import time, pyperclip

press = input()                                                     #first Enter press to start

print('Timer Started!')
startTime = time.time()
lastTime = startTime                                                #time at which last lap ended
lap_num = 1
laps = []
try:
    while(True):
        press = input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        lapPrint = 'Lap #%s ' %str(lap_num)
        totalTimePrint = str(totalTime).rjust(5)
        lapTimePrint = ' (%s)' % str(lapTime).rjust(5)
        finalPrint = lapPrint + totalTimePrint + lapTimePrint
        print(finalPrint)
        laps.append(finalPrint)
        lastTime = time.time()
        lap_num += 1
except KeyboardInterrupt:                                       #taking care of Ctrl+C termination
    print('Done!')

output = '\n'.join(laps)                
pyperclip.copy(output)                                          #copying contens to clipboard