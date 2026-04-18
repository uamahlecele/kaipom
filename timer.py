import time
from datetime import datetime

def countdown_timer(t_seconds):
    t_minutes = t_seconds * 60

    """Count down section of my code"""
    while t_minutes:
        mins, secs = divmod(t_minutes, 60) # divmod returns quotient and remainder of the division of the first argument with the second. Returns a tuple.
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        
        print(timer, end='\r')  # Overwrite the line each second by putting cursor back to the beginning of the line.
        
        time.sleep(1)

        t_minutes -= 1

    print("End of session.")
    
    notes = input("What have you learnt so far? ") # I want to store these notes in a json/ csv file. 

    return notes

# countdown_timer(int(minutes))