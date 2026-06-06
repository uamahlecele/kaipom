"""Lena iMain file yam' essentially and is where everything will run."""

from rich.progress import Progress, track
from datetime import datetime
import json
import time
from rich import print
from rich.markdown import Markdown
from rich.console import Console
from rich.progress import Progress
from rich.progress import BarColumn,TimeRemainingColumn
import argparse
from kaipom.timer import Timer
from kaipom.notes import Notes
from pathlib import Path

from kaipom.quote import Quotes

q = Quotes()

home_dir = Path.home()
console =  Console()


def main():
    
    namhlanje = date_formatter() # I'll use this date to later catalogue in my json file
    start_time = datetime.now()

    args = parsing_ama_argument()
    start_time = start_time.strftime("%R") # %R Shorthand for digital format.

    if args.command == 'study':
        print("")
        
        heading = """# Study Session"""
        current_date = f"### {date_formatter()}"
        current_date = Markdown(current_date)

        mark_down = Markdown(heading)
   
        console.print(mark_down)

        print("")

        console.print(current_date)

        print("")
        print(f"Pomodoro: {args.minutes} minutes") 
    
        if args.minutes != 25:
            print(f"Break duration: 10 Minutes")
            
        else:
             print(f"Break duration: 5 Minutes")
        
        print("")

        # Quote

        console.print(q.random_quote())

        print("")
   
        time.sleep(1) # Adds 3 second delay to prep.

        while True:

            """Main Pomodoro Study Loop"""
            my_study_session = Timer(args.hour,args.minutes)

            notes = my_study_session.study_countdown()
            my_study_session.break_countdown() 
        
            # notes = countdown_timer(args.minutes, args.hour)
            end_time = datetime.now()
            end_time = end_time.strftime("%R")
            
            study_session_dict = {"date": str(namhlanje), "study_duration": f"{args.minutes} minutes", "start_time": start_time, "end_time": end_time, "notes": notes}
            uniq_json = f"{namhlanje}"

            with open(f"{home_dir}/Desktop/kaipom/notes/{uniq_json}-{start_time}.json", "w") as file: # Storing the files in the notes folder
                json.dump(study_session_dict, file)

                break
    
    elif args.command == "notes":
        n = Notes()
        n.get_all_notes()


def date_formatter():

    """Formats todays date and time into
    a prettier, more legible format."""

    namhlanje = datetime.today()
    
    return f"{namhlanje.strftime("%d-%B-%Y")}"
        

def parsing_ama_argument(args = None):
     
    parser = argparse.ArgumentParser(description = 'Study tool that helps me study using the Pomodoro Technique') # This instantiates the ArgumentParser class
    subparsers = parser.add_subparsers(dest = 'command') # dest is where the value of the argument is found using dot notation

    # STUDY TIME (25/50)

    parser_study = subparsers.add_parser('study', help = 'Pomodoro study duration. 25 or 50.')

    parser_study.add_argument('minutes', type = int, choices = [25,50,1], help= 'Choose a study time between 25 (Minutes) or 50 (Minutes)')
    parser_study.add_argument('--hour', default = 1, type = int, choices = [1,2,3,4,5,6], help = 'How long the entire study sessions duration will be for.')

    # NOTES

    parser_notes = subparsers.add_parser('notes', help = 'Take a look at your past study notes.')

    parser_notes.add_argument('--notes', type = str, help = 'See your notes from a specific date or look at them holistically to see what you\'ve learnt.')

    # creates them all for us and stores it into the args variable

    # QUIZ using RAG

    # parser_notes = subparsers.add_parser('quiz', help = 'Generate a quiz based on what you\'ve learnt so far.')

    # parser_notes.add_argument('--random', type = str, help = 'See your notes from a specific date or look at them holistically to see what you\'ve learnt.')

    # args = parser.parse_args() 

    return parser.parse_args(args)



if __name__ == "__main__":
    main()