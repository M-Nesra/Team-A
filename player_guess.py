def guess_checker(guess, country, guessed_letters, wrong_guesses, score):
    """
    this function simply validates the player's guess while updating the wrong_guesses and score


    Attributes:
        guess (str): The player's input-ed letter
        country (str): The correct country's name
        guessed_letters (set): Set of previously guessed letters
        wrong_guesses (int): Count of wrong guesses
        score (int): Current score.

    Returns:
        tuple: updates guessed_letters, wrong_guesses, score, 
    """
    
    """

    CREATE A mock function 

    """

    guess = guess.strip().lower()
    country_lower = country.lower()

    # .isalpha helps identify whether the input is a valid letter or attainst the same length as the country
    if not guess.isalpha() or len(guess) != 1:
        print("Invalid input. Please guess a single letter.")
        return guessed_letters, wrong_guesses, score
   
   
    # Correct guess
    if guess in country_lower:
        guessed_letters.add(guess)
        mock_display_word_state(country, guessed_letters)
        print(f"{guess.upper()}' is correct!")
    else:
        # Incorrect guess
        wrong_guesses += 1
        score = adjust_score(score, "wrong_guess")
        print(f"{guess.upper()}' is incorrect. -10 points. Score: {score}")

    # Loss by incorrect guesses
    if wrong_guesses >= 6:
        print(f"Game Over. The correct country was: {country}")
        return guessed_letters, wrong_guesses, score

    # Loss by score exhaustion
    if score <= 0:
        print(f"You’ve run out of points. The country was: {country}")
        return guessed_letters, wrong_guesses, score

    return guessed_letters, wrong_guesses, score

