# Save the Watermelon – Test Plan (Progression 4)

This document outlines how the game was manually tested to verify that it works as designed.  
Testing was performed by running the program from the terminal and validating behavior against expected results.

---

## 1. How to Run the Game

From the project root directory:

    python -m src.game

This launches the **Save the Watermelon** game in the terminal.

---

## 2. Test Plan Overview

### Purpose
The goal of testing was to ensure that all main gameplay features work correctly and that invalid inputs are handled gracefully.

### Objectives
- Verify correct letter guessing, word reveal, and slice reduction logic  
- Validate user input (only single alphabetic characters accepted)  
- Confirm win and lose messages display correctly  
- Ensure replay and exit logic function as expected

### Scope
This test plan covers **manual testing** of:
- Input validation  
- Correct and incorrect guesses  
- Slice counter logic  
- Game loop (win/lose and replay conditions)

---

## 3. Test Matrix

| # | Test Area | Test Input | Expected Result | Actual Result |
|---|------------|-------------|-----------------|----------------|
| 1 | Valid single-letter input | `a` | Accepted; updates word or slices | ✅ Works as expected |
| 2 | Invalid multi-character | `ab` | Shows validation message | ✅ Displays “Please enter exactly one alphabetic letter (a–z).” |
| 3 | Non-alphabetic input | `3`, `?`, `!` | Rejected with validation message | ✅ Works correctly |
| 4 | Leading/trailing spaces | `  b  ` | Normalized to `b`; accepted | ✅ Works correctly |
| 5 | Case-insensitive input | `A` then `a` | Treated as repeat guess | ✅ Works correctly |
| 6 | Repeat guess | Same letter twice | Message “Already guessed.” | ✅ No slice lost |
| 7 | Correct guess | Letter in word | Revealed in masked word | ✅ Works correctly |
| 8 | Incorrect guess | Letter not in word | Slice count decreases by 1 | ✅ Works correctly |
| 9 | Win condition | All letters guessed | Displays win message | ✅ “You saved the watermelon!” |
| 10 | Lose condition | Use all slices | Displays lose message and reveals word | ✅ Works correctly |
| 11 | Replay | Choose “y” at end | New game starts | ✅ Works correctly |
| 12 | Exit | Choose “n” at end | Game thanks player and exits | ✅ Works correctly |

---

## 4. Manual Test Transcript (Example)

### Test Run: Winning Path

    === Save the Watermelon ===

    Word: _ _ _ _ _ _ _
    Guessed: (none)
    Slices left: 6

    Guess a letter: s
    Wrong answer, Sliced! Remaining turns: 

    Word: _ _ _ _ _ _ _
    Guessed: s
    Slices left: 5
    
    Guess a letter: a
    Wrong answer, Sliced! Remaining turns: 4
    
    Word: _ _ _ _ _ _ _
    Guessed: a s
    Slices left: 4
    
    Guess a letter: o
    Good job!
    
    Word: _ _ _ _ _ _ o
    Guessed: a o s
    Slices left: 4
    
    Guess a letter: r
    Good job!
    
    Word: _ _ r r _ _ o
    Guessed: a o r s
    Slices left: 4
    
    Guess a letter: r
    Already guessed.
    
    Word: _ _ r r _ _ o
    Guessed: a o r s
    Slices left: 4
    
    Guess a letter: b
    Good job!
    
    Word: b _ r r _ _ o
    Guessed: a b o r s
    Slices left: 4
    
    Guess a letter: u
    Good job!
    
    Word: b u r r _ _ o
    Guessed: a b o r s u
    Slices left: 4
    
    Guess a letter: i
    Good job!
    
    Word: b u r r i _ o
    Guessed: a b i o r s u
    Slices left: 4
    
    Guess a letter: t
    Good job!
    
    You saved the watermelon, good work! The word was: burrito
    
    Play again? (y/n): y

### Test Run: Losing Path

    === Save the Watermelon ===

    Word: _ _ _ _ _
    Guessed: (none)
    Slices left: 6
    
    Guess a letter: 6
    Please enter exactly one alphabetic letter (a–z).
    Guess a letter: zz
    Please enter exactly one alphabetic letter (a–z).
    Guess a letter: a
    Good job!
    
    Word: _ a _ _ _
    Guessed: a
    Slices left: 6
    
    Guess a letter: r
    Good job!
    
    Word: _ a r _ _
    Guessed: a r
    Slices left: 6
    
    Guess a letter: l
    Wrong answer, Sliced! Remaining turns: 5
    
    Word: _ a r _ _
    Guessed: a l r
    Slices left: 5
    
    Guess a letter: m
    Wrong answer, Sliced! Remaining turns: 4
    
    Word: _ a r _ _
    Guessed: a l m r
    Slices left: 4
    
    Guess a letter: p
    Wrong answer, Sliced! Remaining turns: 3
    
    Word: _ a r _ _
    Guessed: a l m p r
    Slices left: 3
    
    Guess a letter: z
    Wrong answer, Sliced! Remaining turns: 2
    
    Word: _ a r _ _
    Guessed: a l m p r z
    Slices left: 2
    
    Guess a letter: x
    Wrong answer, Sliced! Remaining turns: 1
    
    Word: _ a r _ _
    Guessed: a l m p r x z
    Slices left: 1
    
    Guess a letter: t
    Wrong answer, Sliced! Remaining turns: 0
    
    Whoops, the watermelon was sliced. You lose! The word was: carne
    
    Play again? (y/n): 

---

## 5. Summary

| Area | Result |
|------|---------|
| Input validation | ✅ Working correctly |
| Slice counter | ✅ Decreases on wrong guesses |
| Win/Lose messages | ✅ Display correctly |
| Replay option | ✅ Working |
| User experience | ✅ Clear prompts and feedback |

**All manual tests passed.**  
The game behaves as described in the design and pseudocode documentation.

---

*End of Test Plan*



