import time
import winsound

"""
Activity: Create a metronome script that plays a beep at the specified speed in beats per minute

Ask the user how many BPM
Play beeps using winsound.Beep(Hz,ms)
Use time.sleep(t) to wait for next beep
Keep repeating with no end to script

Note: Make sure to take into account the duration of each beep when waiting for the next beep
"""

#Ask for metronome BPM
bpm = int(input("How many BPM?"))

#Find time between beats
t = (60/bpm) - 0.1 #-0.1 because duration of beep is 0.1s

while True:
    winsound.Beep(1000,100) #1000Hz, 100ms duration
    time.sleep(t) #Wait for next beep