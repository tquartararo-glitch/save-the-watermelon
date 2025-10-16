# Pseudocode --> layout/ description of what the code will do

CONST MAX_SLICES <-- 6


### pick a random word from WORD_LIST 
FUNCTION SELECT_SECRET_WORD() --> string
    RETURN RANDOM_CHOICE(WORD_LIST)

### validate that the input is 1 letter and an alpha character, remove leading or trailing spaces + normalize for upper/lowercase
FUNCTION NORMALIZE_GUESS(text) --> char | NONE
    s <-- LOWER(TRIM(test))
    IF LENGTH (s)  != 1 THEN RETURN NONE
    IF NOT IS_ALPHA(s) THEN RETURN NONE
    RETURN s

### function to prompt for letter input 
FUNCTION PROMPT_FOR_LETTER() --> char
    LOOP 
        raw <-- INPUT("Guess a letter: ")
        letter <-- NORMALIZE_GUESS(raw)
        IF letter  IS NONE THEN
            DISPLAY "Please enter exactly one alphabetic letter (a-z)."
            CONTINUE
        RETURN letter

### function to add guessed letters
FUNCTION RENDER_MASK(secret, guessed) --> strings
    out <-- EMPTY_STRING
    FOR EACH c IN secret
        IF IS_ALPHA(c) AND c NOT IN guessed THEN
            out <-- out + "_"
        ELSE
            out <-- + c
    RETURN out

### function to process the guesses (add chosen letter, add to revealed letter set, remove a slice)
FUNCTION APPLY_GUESS(secret, guessed, slices, letter) --> (guessed, slices, hit, repeat)
    IF letter IN  guessed THEN
        RETURN (guessed, slices, FALSE, TRUE)
    guessed <-- COPY_SET (guessed) 
    ADD letter TO guessed
    IF  letter IN  secret THEN
        RETURN (guessed, slices, TRUE, FALSE)
    ELSE
        RETURN (guessed, MAX(0, slices - 1), FALSE, FALSE)

###  function to facilitate each round of play
FUNCTION PLAY_ONE_ROUND(secret) --> bool
    guessed <-- 0
    slices <-- MAX_SLICES
    WHILE slices > 0 AND NOT IS_WIN(secret, guessed)
        DISPLAY RENDER_STATE(secret, guessed, slices)
        letter <-- PROMPT_FOR_LETTER()
        (guessed, slices, hit, repeat) <-- APPLY_GUESS(secret, guessed, slices, letter)
        IF repeat THEN
            DISPLAY "Already guessed."
            CONTINUE
        IF hit THEN
            DISPLAY "Good job!"
        ELSE
            DISPLAY "Wrong answer, Sliced! Remaining turns: " + TO_STRING(slices)
        ENDWHILE
    IF IS_WIN (secret, guessed) THEN
        DISPLAY "You saved the watermelon, good work!"
    ELSE
        DISPLAY "Whoops, the watermelon was sliced, You loose!  The word was: " + secret
        RETURN FALSE

### Main loop to run game
FUNCTION MAIN_GAME_LOOP()
    load words from RANDOM_CHOICE() 
        secret < -- SELECT_SECRET_WORD()
        _WON <-- PLAY_ONE_ROUND()
        again <-- LOWER(TRIM(INPUT("Play again? (y/n): ")))
    UNTIL again != "y"
    DISPLAY "Thanks for playing the Watermelon game!"
END FUNCTION



    
