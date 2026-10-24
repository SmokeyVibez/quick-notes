# Quick Notes

A small notes app for Linux (KDE). One window, one menu:

- **Add a note**
- **Read my notes** (shown numbered)
- **Edit a note** (opens with the note's current words already in the box)
- **Delete a note**

After each one, the menu comes back. **Cancel** on the menu closes the app.

Every window carries the title "Quick Notes" and the notes icon, and the windows use whatever KDE theme your computer runs — the app looks like it belongs on your machine. The look is deliberately plain, in the spirit of Windows 95: simple, but it works.

Notes are saved in a plain text file named `notebook.txt` that lives in the same folder as the app. Nothing is sent anywhere — everything stays on your computer.


<img width="570" height="154" alt="quicknotesapp2" src="https://github.com/user-attachments/assets/0b0fcda5-86fc-40a8-8a66-aa55a523942b" />
<img width="284" height="315" alt="quicknotesapp" src="https://github.com/user-attachments/assets/13170966-d5ac-4eb4-83b0-5a513b58f81c" />


## What you need

- Linux with KDE (the app's windows are drawn by `kdialog`, which comes with KDE)

## The files in this folder

| File | What it is |
| --- | --- |
| `quicknotes` | The app itself |
| `Quick Notes.desktop` | The launcher — the icon you click to start the app |
| `notebook.txt` | Your notes. Created beside the app the first time you save a note |
| `README.md` | This file |

## Setting it up

1. Put this folder where you want the app to live (your home folder works).
2. Open `Quick Notes.desktop` in a text editor and look at the `Exec=` line. It must point at the `quicknotes` file in the folder's new home. Example: if the folder sits in your home folder, the line reads `Exec=/home/yourname/quicknotes-app/quicknotes` — change `yourname` to yours.
3. Copy `Quick Notes.desktop` to your Desktop. (Optional: also copy it to `~/.local/share/applications` and it shows up in your app menu too.)
4. Double-click the desktop icon. The app starts with a blank notebook; your first note creates `notebook.txt`.

## Updating to a newer version

You only replace **one file**: the `quicknotes` program file in the folder.

- The launcher does **not** change when the app changes — its lines only hold the app's name, its picture, and where the program file sits. You do not need to copy it again.
- Your `notebook.txt` is untouched by an update. Your notes stay.
- The launcher only ever needs editing again if you move or rename the folder.

## Version

4.4.3 — menu loop, edit and delete built in, titled and sized windows with the notes icon, packaged as a single file with PyInstaller.

---

Made by SmokeyVibez. Every line of the code was written and hand-typed by him. Io — his AI tutor, on Muse — taught and guided; the code is his.
