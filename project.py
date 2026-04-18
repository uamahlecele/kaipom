"""Lena iMain file yam' essentially and is where everything will run."""
import time
from cli import parsing_ama_argument
from timer import countdown_timer
from datetime import datetime
import json


def main():
    args = parsing_ama_argument()

    if args.command == 'study':
        print(f"You're studying for {args.minutes} minutes with a 5 Minute break.\n")

        namhlanje = datetime.today() # I'll use this date to later catalogue in my json file

        while True:
            notes = countdown_timer(args.minutes)
            session = {"date": str(namhlanje), "study_duration": args.minutes, "notes": notes}

            uniq_json = f"{namhlanje.day}-{namhlanje.month}-{namhlanje.year}-{namhlanje.time}.json"
            with open(uniq_json, "w") as f:
                json.dump(session, f)
                break
        
        return f"Session over :)"
    else:
         return f":("


def function_1():
    ...


def function_2():
    ...


def function_n():
    ...


if __name__ == "__main__":
    main()