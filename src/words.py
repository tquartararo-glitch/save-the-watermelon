"""
word sourcing for the Save the Watermelon game.
- DEFAULT WORD_LIST keeps the list self-contained.
- load_words_from_file lets you later use data/words.txt.
- select_secret_word picks a random word (lowercased).
"""
from pathlib import Path    # used for cross-platform file sharing / handling, needed if we later add a file for choice word reference
import random               # used for random number generation

# list of words from which to find a random word
WORD_LIST: list[str] = [
    "tacos", "burrito", "pollo", "carne", "adobada",
    "pizza", "pasta", "calzone", "wine", "olives",
    "ski", "snowboard", "mountain", "blizzard", "chairlift",
]

# Load one word per line (ignore blanks/#comments) if file exists otherwise use whats in the WORD_LIST
def load_words_from_file(path: Path) -> list[str]:

    words: list[str] = []
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines(): # read file & decode ast UTF-8 text (default text encoding)
            t = line.strip().lower()
            if not t or t.startswith("#"):
                continue
            words.append(t)
    return words or WORD_LIST

# Pick a random word from provided list or default WORD_LIST.
def select_secret_word(source: list[str] | None = None) -> str:     #returns the list if found otherwise nothing
    pool = source if source else WORD_LIST                          # if list/source exists, will assign to pool, otherwise pool default to fixed list
    return random.choice(pool).lower()                              # returns a random selection from pool
