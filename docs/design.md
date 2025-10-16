# Progression 1 -- Design

# Problem Statement & target Audience
Build a terminal-based word-guessing game where the player must "Save the Watermelon" by guessing letters before the "slice counter" runs out.

# Game rules & win/lose Conditions
 - Randomly selected word
 - Player enters letters one at a time
   - If the letters are correct, the correct letter will populate / reveal in the build of the word
   - If the letters chosen are incorrect, the player will take a slice out of the watermelon
 - The player wins if they chose the correct letters to complete the word before running out of slices
 - The player loses if they run out of slices before completing the word completely
 - Afte the game ends, we will prompt the player to ask if they want to replay

# Core Features (must-haves) 
- Random word selection (from a built in referenced list)
- Validation that the user inputs are correct (single letter, alphabetic character, no duplication)
- Masked rendering, slice counter, list of guessed letters 
- Clear console (prompts, messages, replay option)
- Organized repository (not one big file)
- Standard library (no third party packages required)


# Stretch goals (nice-to-have)
- ASCII art stages
- difficulty levels
- hints
- word categories 
- scoreboard 

# Basic flow 
1. Initialize the game: choose secret word; set 'slices = MAX_SLICES'; 'guessed = 0'.
2. Loop while 'slices > 0' and not win:
   - Render masked word, guessed letters, remaining slices
   - Prompt for a single letter, validate the input (alpha, single).
   - If already guessed: warn and continue
   - Else add to 'guessed':
     - If letter in secret: show success message.
     - Else: 'slides -=1', show "sliced" message.
3. End: if win -> celebrate; else -> reveal word.
4. Ask to replay (yes or no)

# Data Design: word storage, revealed letters, guessed letters, remaining slices
1. Word list: contains predefined list of secret words
- WORD_LIST --> [x, y, z,...]
 
2. Word storage: the random word chosen for the current round. 
- secret_word --> (str)

3. Revealed letters: generated each turn based on which letters have been guessed thus far.
- revealed_letters --> (derived string)
- not stored permanently, recomputed each loop

4. Guessed letters: keeps track of every unique letter the player has entered.
- guessed_letters --> (set of str)

5. Remaining slices: like remaining lives, how many slices remain until player runs out of guesses
- remaining_slices --> (int)


# Module/function responsibilities
1. Game flow & user interaction: scr/game.py --> handles printing, calling logic functions & asking for replay
- main() --> main entry point, contains high level loop & handles replay
- play_one_round() --> controls a single game round: setup, guessing loop & win/loss check
- prompt_letter() --> gets a single alpha letter from the user, rejects invalid or duplicate entries

2. Core rules: scr/logic.py 
- MAX_SLICES --> constant definition of slices / lives
- normalize_guess(letter: str) -> str | None  --> ensures a single lowercase alpha character
- render_mask(secret: str, guessed: set[str]) --> str builds a masked string
- is_win(secret: str, guessed: set[str]) -> bool --> returns True if all letters revealed.
- apply_guess(secret: str, guessed: set[str], slides: int, guess: str) --> updates the guessed set, adjusts the slices and returns updated flags (hit, repeat, etc.)
- render_state(secret, guessed, slides) --> formatted string showing progress for printed / console output

3. Word management: scr/words.py
- WORD_LIST --> default in-code list of words
- select_secret_words(source=None) --> randomly selects a word from WORD_LIST

4. Testing the core functions: tests/test_logic.py
- Unit test for render_mask, apply_guess, is_win, etc.

5. Folder: docs --> design, planning & test outcomes

