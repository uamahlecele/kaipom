"""Kule-Module ngizofaka ama-commands azosetshenziswa i-Program"""

import json
import time
import argparse

def parsing_ama_argument():
    
    parser = argparse.ArgumentParser(description = 'Study tool that helps me study using the Pomodoro Technique') # This instantiates the ArgumentParser class
    subparsers = parser.add_subparsers(dest = 'command') # dest is where the value of the argument is found using dot notation

    # STUDY TIME (25/50)

    parser_study = subparsers.add_parser('study', help='Pomodoro study duration. 25 or 50.')

    parser_study.add_argument('minutes', type= int, choices = [25,50,1], help= 'Choose a study time between 25 (Minutes) or 50 (Minutes)')

    # NOTES

    parser_notes = subparsers.add_parser('notes', help= 'Take a look at your past study notes.')

    parser_notes.add_argument('--notes', type=str, help= 'See your notes from a specific date or look at them holistically to see what you\'ve learnt.')

    args = parser.parse_args()  # creates them all for us and stores it into the args variable

    
    return args

# while True:
#     print("Welcome to KaiPom: Enter your pomodoro study method duration: ")
#     user_pom= input("Format (mm/mm): ")
#     try:
#         minutes, minutes_break = user_pom.split("/")
#         minutes  = (int(minutes)*60)
#         minutes_break = int(minutes_break)
#     except ValueError:
#         print("Please use the format mm/mm.")
#     try:
#         user_duration = int(input("How many hour(s)?: "))
#         break
#     except ValueError:
#         print("Please use numbers only.")


# print(f"You're studying for {notes} minutes with a 5 Minute break.\n")

# print("Time on the clock: \n24:59")

# e.g Input
# Pomodoro session 25/5 or 50/ 10 
# For How long: 50 Min, 1 Hour, 4 Hours etc.

# parser.add_argument('--notes', metavar='recap', type = str, help ='See your notes')
# parser.add_argument('notes', metavar='recap', type = str, help ='See your notes')

# I might need to add subcommands.


# parser.add_subparsers() 






# def countdown_timer(t_seconds):
#     """Count down section of my code"""
#     while t_seconds:
#         mins, secs = divmod(t_seconds, 60) # divmod returns quotient and remainder of the division of the first argument with the second in a tuple.
#         timer = '{:02d}:{:02d}'.format(mins, secs)
        
#         print(timer, end='\r')  # Overwrite the line each second by putting cursor back to the beginning of the line.
        
#         time.sleep(1)

#         t_seconds -= 1

#     print("End of first session: ")

#     notes = input("What have you learnt so far? ") # I want to store these notes in a json/ csv file. 

# countdown_timer(int(minutes))

# """Should I use OOP for this? I think so."""

# """I need to figure out a way to trigger a seperate Hour long study session in Hours, similar to the mini timer."""

# """Code to store my notes in a csv or json file. And code to load it up into my terminal."""




