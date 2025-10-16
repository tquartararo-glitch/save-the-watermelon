"""
Terminal user interface.
  - MAIN_GAME_LOOP
  - PLAY_ONE_ROUND
  - PROMPT_FOR_LETTER
"""

from pathlib import Path                                        # allow access to data/words.txt
from . import logic                                             # import logic functions from logic.py, called multiple times throughout each turn
from .words import load_words_from_file, select_secret_word     # import 2 functions from words.py, called once per game

# Prompt & loop until 1 correct letter is input by the user
def prompt_for_letter() -> str:
    while True:
        raw = input("Guess a letter: ")
        letter = logic.normalize_guess(raw)
        if letter is not None:
            return letter
        print("Please enter exactly one alphabetic letter (a–z).")

# Run a single round. Return True if Win, False if Sliced.
def play_one_round(secret: str) -> bool:

    guessed: set[str] = set()
    slices = logic.MAX_SLICES

    print("\n=== Save the Watermelon ===")

    while slices > 0 and not logic.is_win(secret, guessed):
        # Display current state
        print(logic.render_state(secret, guessed, slices))

        # Prompt and apply guess
        letter = prompt_for_letter()
        guessed, slices, hit, repeat = logic.apply_guess(secret, guessed, slices, letter)

        # Messages  on logic of input
        if repeat:
            print("Already guessed.")
            continue
        if hit:
            print("Good job!")
        else:
            print(f"Wrong answer, Sliced! Remaining turns: {slices}")

    if logic.is_win(secret, guessed):
        print(f"\nYou saved the watermelon, good work! The word was: {secret}\n")
        return True
    else:
        print(f"\nWhoops, the watermelon was sliced. You lose! The word was: {secret}\n")
        return False

# Main replay loop, optionally loads words from data/words.txt (if it were to be populated).
def main() -> None:
    data_path = Path(__file__).resolve().parent.parent / "data" / "words.txt"
    words = load_words_from_file(data_path)

    while True:
        secret = select_secret_word(words)
        _won = play_one_round(secret)
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing the Watermelon game!")
            break

if __name__ == "__main__":
    main()
