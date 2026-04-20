"""Lena iMain file yam' essentially and is where everything will run."""

from cli import parsing_ama_argument
from timer import countdown_timer
from datetime import datetime
import json
import time
from pathlib import Path
from tabulate import tabulate
from rich import print
from rich.markdown import Markdown
from rich.console import Console




console =  Console()

def main():
    
    namhlanje = date_formatter() # I'll use this date to later catalogue in my json file
    manje = datetime.now()

    args = parsing_ama_argument()
    start_time = manje.strftime("%R") # %R Shorthand for digital format.

    if args.command == 'study':
        print("")
        
        heading = """# Study Session"""
        mark_down = Markdown(heading)
        line = "_"
   
        console.print(mark_down)
      
        print(f"Pomodoro: {args.minutes} minutes") 
        print(f"Total Session: {args.hour} hour(s)")
    
        if args.minutes != 25:
            print(f"Break duration: 10 Minutes")
        else:
             print(f"Break duration: 5 Minutes")
        
        print("")
   
        time.sleep(2) # Adds 3 second delay to prep.

        while True:

            """Main Clock Loop"""
            
            # big_clock = overall_study_duration_count_down(args.hour)

            notes = countdown_timer(args.minutes, args.hour)
            
            session = {"date": str(namhlanje), "study_duration": f"{args.minutes} minute", "start_time": start_time, "notes": notes}
            uniq_json = f"{namhlanje}"

            with open(f"/Users/amahlecele/Desktop/kaipom/notes/{uniq_json}-{start_time}.json", "w") as file: # Storing the files in the notes folder
                json.dump(session, file)

                break
        
        return f"Session over :)"
    
    elif args.command == "notes":
        notes_table()


def date_formatter():
    "Formats todays date and time into a prettier, more legible format."

    namhlanje = datetime.today()
    
    return f"{namhlanje.strftime("%d-%B-%Y")}"
        

def notes_table():

    """This function displays all of my study sessions."""
    
    print("")
    heading = """# Study Log """


    md = Markdown(heading)
    console.print(md)

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


def function_n():
    ...


if __name__ == "__main__":
    main()