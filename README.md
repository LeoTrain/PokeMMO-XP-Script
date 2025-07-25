# PokeMMO XP Script

This is a GUI script made to automate XP farming in **PokeMMO**.
I built it so I don’t have to grind manually anymore.

The project is written in **Python**, mainly using:

* `pyautogui` to send keyboard inputs to the game.
* `NSWorkspace` from `AppKit` to focus the PokeMMO window so it actually receives the inputs.

---

## Usage

Run:

```bash
make
```

A GUI will open with a green button. Click it to start the bot.

Note: I'm currently on a **Mac M1** with a **2560x1600** resolution.
PokeMMO must be placed on the **right half** of the screen, meaning from coordinates `1280x0` to `2560x1600`.

---

## TODO

* [ ] Make it easier to launch
  → Is it already simple enough? Probably no need for a full executable.

* [ ] Add more user information and guidance

* [ ] Support reading long text
  (For future features like stopping when out of PP, using different moves, etc.)

* [ ] Finish "go to center" script and add it to the GUI

  * [ ] Handle repel wearing off without losing position tracking

* [ ] Send inputs only to the PokeMMO window
  → Currently not working on macOS
  → Possible workaround: run it in a VM or on another machine

* [ ] Add setup option to define a new pixel position, or enter PokeMMO window size and adjust positions automatically

* [ ] Double-check the screen size note in the Usage section

---

## Done

* [x] Write this README

* [x] Choose Python version
  → Currently using `python3.13.5`
  → The `mss` module is no longer needed

* [x] Add logging to functions and write logs to a file
  → `_to_log()` function added

* [x] Create `.gitignore` and initialize the repo
  → Ignoring `env/` only

* [x] Improve the Tkinter GUI
  → Better colors and XP bot log display

* [x] Refactor into classes and separate files
  → `Moving`, `XpBot`, and `App` classes

---

Let me know if you want help generating a Markdown preview or turning this into a proper release setup.
