"""
Game logic structure & functions

Implements:
- MAX_SLICES
- normalize_guess(text)
- render_mask(secret, guessed)
- render_state(secret, guessed, slices)
- is_win(secret, guessed)
- apply_guess(secret, guessed, slices, letter)
"""

# CONST MAX_SLICES <-- 6
MAX_SLICES: int = 6

 # Clean input of guess, trim & lower case, must be exactly one a–z character. Return cleaned letter or None.
def normalize_guess(text: str | None) -> str | None:
    if text is None:
        return None
    s = text.strip().lower()
    if len(s) != 1:
        return None
    if not s.isalpha():
        return None
    return s

## Build the masked string; show letters that are guessed, '_' for hidden letters.  Non-alpha chars (if any) pass through unmasked.
def render_mask(secret, guessed):
    out = ""
    for c in secret:
        out += c if c in guessed else "_"
    return out

# Return True if all letters in secret have been guessed
def is_win(secret, guessed):
    return all(c in guessed or not c.isalpha() for c in secret)

"""
Apply a guess and return (new_guessed, new_slices, hit, repeat).
    - If repeat guess: state unchanged, repeat=True, hit=False.
    - If new and in secret: add to guessed, hit=True, slices unchanged.
    - If new and not in secret: add to guessed, hit=False, slices -= 1 (not below 0). 
"""

def apply_guess(
    secret: str,
    guessed: set[str],
    slices: int,
    letter: str,
) -> tuple[set[str], int, bool, bool]:

    if letter in guessed:
        return guessed, slices, False, True

    new_guessed = set(guessed)
    new_guessed.add(letter)

    if letter in secret:
        return new_guessed, slices, True, False
    else:
        return new_guessed, max(0, slices - 1), False, False

# Return a formatted block for console display (kept pure; game.py prints it).
def render_state(secret: str, guessed: set[str], slices: int) -> str:

    masked = render_mask(secret, guessed)
    guessed_list = " ".join(sorted(guessed)) if guessed else "(none)"
    spaced_masked = " ".join(masked)
    return (
        f"\nWord: {spaced_masked}\n"
        f"Guessed: {guessed_list}\n"
        f"Slices left: {slices}\n"
    )
