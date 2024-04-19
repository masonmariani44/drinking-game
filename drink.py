
import random
import time
import glob

# people are saying this sound stuff might not work on linux/mac but idc. just making this for pc bros
# https://stackoverflow.com/questions/16573051/sound-alarm-when-code-finishes
#import os
import winsound

import tkinter as tk
from RangeSlider.RangeSlider import RangeSliderH 



"""
Drinking game for the guys. 

Upon program start, it will prompt the user for a time interval. Once a time interval is chosen
a random time within the interval is chosen, and a timer starts counting down to said time. Once
the timer goes off, you must STOP EVERYTHING YOURE DOING and drink, and a new time is chosen and timer set.
"""



def main():
    # prompt user for time
    start_mins = int(input("Input start time (mins): "))
    end_mins = int(input("Input end time (mins): "))

    #list and prompt for alarm sound
    print("Choose an alarm sound (integer number):")
    sound_list = glob.glob('./*.wav')
    i = 0
    for file in sound_list:
        print(f"\t({i})\t{file}")
        i += 1
    print(f"\t({i})\tDEFAULT")
    sound = int(input())


    # main loop
    round = 1
    while True:

        print(f"Round: {round}")

        # choose time in interval
        chosen_mins = random.randint(start_mins, end_mins)
        chosen_secs = chosen_mins * 60

        # start timer
        countdown_secs = chosen_secs
        while countdown_secs:
            mins, secs = divmod(countdown_secs, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            countdown_secs -= 1
        
        #finish timer
        print("Time's up")

        if sound < 0 or sound > len(sound_list):
            winsound.Beep(440, 1000) #freq, duration (ms)
        else:
            winsound.PlaySound(sound_list[sound], 0)
    
        round += 1





if __name__ == "__main__":
    main()