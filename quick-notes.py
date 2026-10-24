#!/usr/bin/env python3
# Version 4.4.3 - knotes icon in every window
# Version 4.4.2 - find its folder when packaged
# Version 4.4.1 - missing endings added to delete and edit
# Version 4.4.0 - windows sizes set with geometry
# Version 4.3.0 - edit a note from the menu
# Version 4.2.0 - windows are titled Quick Notes
# Version 4.1.0 - the menu comes back after each choice
# Version 4.0.0 - delete a note from the menu
# Version 3.1.1 - notes file renamed to notebook.txt
# Version 3.1.0 - read shows the notes numbered
# Version 3.0.0 - menu at startup: add a note or read the notebook
# Version 2.0.1 - pressing Cancel no long saves an empty note
# Version 2.0.0 - saves the note into a notebook file beside the program
# Version 1.0.0 - asks for a note and shows it back


import os
import subprocess
import sys

if getattr(sys, "frozen", False):
    folder = os.path.dirname(os.path.abspath(sys.executable))
else:
    folder = os.path.dirname(os.path.abspath(__file__))
book = os.path.join(folder, "notebook.txt")
while True:
    choice = subprocess.run(["kdialog", "--icon", "knotes", "--title", "Quick Notes", "--menu", "What do you want to do?", "add", "Add a note", "read", "Read my notes", "delete", "Delete a note", "edit", "Edit a note"], capture_output=True, text=True)
    pick = choice.stdout.strip()
    if choice.returncode !=0:
        break
    if pick == "add":
        answer = subprocess.run(["kdialog","--geometry", "560x120", "--icon", "knotes", "--title", "Quick Notes", "--inputbox", "Type your note:"], capture_output=True, text=True)
        note = answer.stdout.strip()
        if answer.returncode == 0:
            with open(book, "a") as f:
                print(note, file=f)
            subprocess.run(["kdialog", "--icon", "knotes", "--title", "Quick Notes", "--msgbox", "You Saved: " + note])
    if pick == "read":
        if os.path.exists( book):
            with open(book, "r") as f:
                notes = f.read()
            lines = notes.splitlines()
            numbered = ""
            count = 1
            for line in lines:
                numbered = numbered + str(count) + ". " + line + "\n"
                count = count + 1
            subprocess.run(["kdialog", "--icon", "knotes", "--title", "Quick Notes", "--msgbox", numbered])
        else:
            subprocess.run(["kdialog", "--icon", "knotes", "--title", "Quick Notes", "--msgbox", "Your notebook is empty."])
    if pick == "delete":
        if os.path.exists(book):
            with open(book, "r") as f:
                notes = f.read()
            lines = notes.splitlines()
            command = ["kdialog", "--geometry", "560x240", "--icon", "knotes", "--title", "Quick Notes", "--menu", "Pick the note to delete:"]
            count = 1
            for line in lines:
                command += [str(count), line]
                count = count + 1
            ask = subprocess.run(command, capture_output=True, text=True)
            if ask.returncode == 0:
                num = int(ask.stdout.strip())
                del lines[num - 1]
                with open(book, "w") as f:
                    for line in lines:
                        print(line, file=f)
                subprocess.run(["kdialog", "--icon", "knotes", "--title", "Quick Notes", "--msgbox", "Deleted."])
        else:
            subprocess.run(["kdialog", "--icon", "knotes", "--title", "Quick Notes", "--msgbox", "Your notebook is empty."])
    if pick == "edit":
        if os.path.exists(book):
            with open(book, "r") as f:
                notes = f.read()
            lines = notes.splitlines()
            command = ["kdialog", "--geometry", "560x240", "--icon", "knotes", "--title", "Quick Notes", "--menu", "Pick the note to edit:"]
            count = 1
            for line in lines:
                command += [str(count), line]
                count = count + 1
            ask = subprocess.run(command, capture_output=True, text=True)
            if ask.returncode == 0:
                num = int(ask.stdout.strip())
                answer = subprocess.run(["kdialog", "--geometry", "560x120", "--icon", "knotes", "--title", "Quick Notes", "--inputbox", "Edit your note:", lines[num - 1]], capture_output=True, text=True)
                if answer.returncode == 0:
                    lines[num - 1] = answer.stdout.strip()
                    with open(book, "w") as f:
                        for line in lines:
                            print(line, file=f)
                    subprocess.run(["kdialog", "--icon", "knotes", "--title", "Quick Notes", "--msgbox", "Edited."])
        else:
            subprocess.run(["kdialog", "--icon", "knotes", "--title", "Quick Notes", "--msgbox", "Your notebook is empty."])



