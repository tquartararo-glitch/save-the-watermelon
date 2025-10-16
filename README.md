# 🍉 Save the Watermelon

## 🧩 Project Description
**Save the Watermelon** is a terminal-based word guessing game written in Python.  
The player must guess the hidden word one letter at a time before the watermelon is completely sliced.  
Each incorrect guess removes a “slice” (life). The goal is to reveal all letters before your slices run out.

This project was built as part of an introductory Python programming course to demonstrate modular design, clean code structure, and GitHub workflow.

---

## ⚙️ How to Run the Game
> 📝 **No external files required** — all words are stored in the built-in `WORD_LIST` inside `src/words.py`.

### Run from terminal
From your project root (the folder that contains `src/`): python -m src.game

## 🕹 Game Features & Rules
- Randomly selects a secret word from the internal `WORD_LIST` each round.
- Displays masked word (e.g., `_ a _ e`) as you guess.
- Each wrong guess slices one piece of the watermelon.
- Input validation for alphabetic letters only.
- Replay option after each game.

### ✨ Stretch Goals (Future Enhancements; may try this weekend if I have time)
- Add ASCII art stages showing the watermelon being sliced.
- Introduce difficulty levels or hints.
- Scoreboard showing history of past game performance.

---

## 🚧 Known Issues / Limitations
- Fixed word list within `src/words.py`. (code structured to add files, but not yet added)
- Must be run from project root directory.

### 🔍 Technical Notes
- No persistent data or scoring between games, the game is fresh with each restart.
- Designed for terminal execution (no GUI).

---

## 🙌 Credits
Developed by **Tony Quartararo**  
Course: *CISC-179 Python Programming*  
Instructor: *Dr. Danish Khan*

### 🧰 Tools & Resources
- Built using Python 3.13 and PyCharm IDE
- Version control with GitHub
- Emoji assets via [Emojipedia](https://emojipedia.org)


