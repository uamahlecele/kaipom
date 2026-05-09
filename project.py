"""Lena iMain file yam' essentially and is where everything will run."""

from rich.progress import Progress, track
from datetime import datetime
import json
import time
from pathlib import Path
from rich import print
from rich.markdown import Markdown
from rich.console import Console
from rich.progress import Progress
from rich.progress import BarColumn,TimeRemainingColumn
import argparse

console =  Console()

def main():
    
    namhlanje = date_formatter() # I'll use this date to later catalogue in my json file
    manje = datetime.now()

    args = parsing_ama_argument()
    start_time = manje.strftime("%R") # %R Shorthand for digital format.

    if args.command == 'study':
        print("")
        
        heading = """# Study Session"""
        current_date = f"### {date_formatter()}"
        current_date = Markdown(current_date)

        mark_down = Markdown(heading)
        line = "_"
   
        console.print(mark_down)

        print("")

        console.print(current_date)

        print("")
        print(f"Pomodoro: {args.minutes} minutes") 
        # print(f"Total Session: {args.hour} hour(s)")
    
        if args.minutes != 25:
            print(f"Break duration: 10 Minutes")
        else:
             print(f"Break duration: 5 Minutes")
        
        print("")
   
        time.sleep(2) # Adds 3 second delay to prep.

        while True:

            """Main Pomodoro Study Loop"""
            
            notes = countdown_timer(args.minutes, args.hour)
            
            study_session_dict = {"date": str(namhlanje), "study_duration": f"{args.minutes} minutes", "start_time": start_time, "notes": notes}
            uniq_json = f"{namhlanje}"

            with open(f"/Users/amahlecele/Desktop/kaipom/notes/{uniq_json}-{start_time}.json", "w") as file: # Storing the files in the notes folder
                json.dump(study_session_dict, file)

                break
        
        return f"The pomodoro session is over :)"
    
    elif args.command == "notes":
        notes_table()


def date_formatter():

    """Formats todays date and time into
    a prettier, more legible format."""

    namhlanje = datetime.today()
    
    return f"{namhlanje.strftime("%d-%B-%Y")}"
        

def notes_table():

    """This function displays all of my study sessions."""
    
    print("")
    heading = """# Study Log """

    md_format = Markdown(heading)
    console.print(md_format)

    notes_folder = Path('/Users/amahlecele/Desktop/kaipom/notes').iterdir()

    for file in notes_folder:
        with open(f"{str(file)}","r") as f:
            data = json.load(f)

            for k,v in data.items(): 
    
                if k == "notes":
                    print(f"+ {k.title()}:\n", end = " ")
                    print("")
                    sentence = v.split(" ")
                    count = 0

                    for word in sentence:
              
                        if count < 15:
                            print(word, end = " ")
                            count += 1 
                        else: 
                            print("") 
                            print(word, end = " ")

                            count = 0  
                            count+=1        
                                
                elif k == "date":
                    date_pretty = v.split("-")
                    date_pretty = " ".join(date_pretty)

                    print(f"+ {k.title()}: {date_pretty}")
                else:
                    print(f"+ {k.title()}: ", v)
                    
        ln = "_"
        print(f"\n{ln*108}")
        print(f"{ln*108}")
        print("")


def countdown_timer(pomodoro_minutes, total_study_session_hours) -> str:

    """Count down Pomodoro section of my code"""

    start = time.monotonic() # My reference point when the timer start to keep track of total passed seconds
    print("Time left: ") 
    if pomodoro_minutes == 25:
        study_break = 5*60
    else:
        study_break = 10*60

    try: 
        total_study_session_hours = (total_study_session_hours*60*60) #Total study duration

        pomodoro_minutes_in_seconds = (pomodoro_minutes * 60) # Convert the minutes I'll receive into seconds
    except ValueError:
        print("Only integers are allowed!")
    

    with Progress(BarColumn(), TimeRemainingColumn()) as progress: # With will close the progress bar once I'm done with it automatically

        study_session = progress.add_task( total= pomodoro_minutes_in_seconds,description= "Pomodoro in session",)
        
        while True:
            elapsed = time.monotonic() - start # How many seconds has it been?
            if elapsed >= pomodoro_minutes_in_seconds:
                progress.update(study_session, completed=pomodoro_minutes_in_seconds) 
                break
            
            progress.update(study_session, completed=elapsed)
            # t_session -= elapsed
            time.sleep(0.1)      
            

    console.print("End of session. ") 
    print("")
    
    notes = input("What have you learnt so far? ")  # I want to store these notes in a json/ csv file. 

    print("")

    start_break = time.monotonic()
    print("Break:") 

    with Progress(BarColumn(),TimeRemainingColumn()) as progress_break: # With will close the progress bar once I'm done with it automatically

        break_session = progress_break.add_task(description= "Break in progress", total=study_break)
        
        while True:
            elapsed = time.monotonic() - start_break # How many seconds has it been?
            if elapsed >= study_break:
                progress_break.update( break_session, completed = study_break) 
                break
            
            progress_break.update(break_session, completed=elapsed)
            # study_break -= elapsed
            time.sleep(0.1)      
    
    console.print("Goodbye!")

    return notes 

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