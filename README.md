# kaipom

Named from joining the two words, Kaizen (Japanese philosophy of continous improvement) & Pomodoro, is command‑line study tool that uses the Pomodoro Technique to help me focus, track my learning, and revisit what I've learnt. 

I noticed sometimes when I didn't have Wifi or data I couldn't use the Youtube Pomodoro videos I liked to study along with and that affected how I learnt, so I decided to build a tool I know that I'll utilise all the time. That's how Kaipom came to be.

## How it works

- You start a session by typing **kp study 25** or **kp study 50**.
- After the session ends you will be prompted with **What have you learnt/done so far?**
- The note entry is then stored in a JSON file with all your details (Start time, End time, Note).
- To retrieve all your notes you type **kp notes**

## Features

- **Pomodoro timer** – Start a 25 or 50 minute focus session.
- **Study notes** – Add notes after each session. View all notes.
<!-- - **Quiz** – Generate a simple quiz from your own notes (local only, no external APIs). -->

## Intallation 
```bash
#install requirement libraries
python3 -m pip install -r requirements.txt
```


## Commands

```bash
# Start a Pomodoro Session
kp study 25
kp study 50 

```
<img width="699" height="320" alt="Screenshot 2026-06-06 at 19 44 38" src="https://github.com/user-attachments/assets/e10ca583-b55f-4f35-ab71-715f4480a2e8" />

# View notes
```bash
kp notes
```

<img width="766" height="224" alt="kp sc" src="https://github.com/user-attachments/assets/e291624a-1145-4d05-b123-62e4d228954d" />




