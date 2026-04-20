import time
from datetime import datetime
import sys
from tqdm import trange # tqdm stands for progress in arabic
from rich.progress import Progress, track
from rich import print
from rich.markdown import Markdown
from rich.console import Console

console = Console()






def countdown_timer(t_seconds, t_session) -> str:

    """Count down Pomodoro section of my code"""


    if t_seconds == 25:
        study_break = 5*60
    else:
        study_break = 10*60


    t_session = (t_session*60) #Total study duration

    t_minutes = (t_seconds * 60) # Convert the minutes I'll receive into seconds
    v = t_minutes

    # while t_session:

    #     total_mins, total_secs = divmod(t_session, 60) # divmod returns quotient and remainder of the division of the first argument with the second. Returns a tuple.
        
    #     total_hours, total_mins = divmod(total_mins, 60)
    #     study_timer = f'{total_hours:02d}:{total_mins:02d}:{total_secs:02d}'
            
    #     print("Time Left:",study_timer, end='\r', flush = True)  # Overwrite the line each second by putting cursor back to the beginning of the line.
        
    #     time.sleep(1) # Creates 1 second delay

    #     t_session -= 1

    while t_minutes:
        # for i in track(range(t_minutes,0,-1), description= f"Pomodoro in progress"):

            mins, secs = divmod(t_minutes, 60) # divmod returns quotient and remainder of the division of the first argument with the second. Returns a tuple.
            timer = '{:02d}:{:02d}'.format(mins, secs) 
            
            print("Time Left:", timer, end='\r')  # Overwrite the line each second by putting cursor back to the beginning of the line.
       
            time.sleep(1) 

            t_minutes-=1

    console.print("End of session. ")

    
    notes = input("What have you learnt so far? ")  # I want to store these notes in a json/ csv file. 

    print("")

    while study_break:
        for i in track(range(study_break,0,-1), description="Break (Phumula): "):
        
            # break_mins, break_secs = divmod(study_break, 60) # divmod returns quotient and remainder of the division of the first argument with the second. Returns a tuple.
            # timer = '{:02d}:{:02d}'.format(break_mins, break_secs) 
            
            # print("Break (Phumula): ", timer, end='\r')  # Overwrite the line each second by putting cursor back to the beginning of the line.
            
            time.sleep(1) 

            study_break -= 1
        

    return notes 