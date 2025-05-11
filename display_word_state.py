def display_word_state(country: str, guessed_letters: str) :
    """
    Displays the current state of the guessed word with underscores for unguessed letters.

    Parameters:
        country (str): The actual country name.
        guessed_letters (set): The set of letters that have been guessed so far.

    Returns:
        str: The current visible state of the word with guessed letters and underscores.
    """
    guessed_set = set(guessed_letters.lower())  # Convert string to a set
    display = ""

    for letter in country:
        if letter.lower() in guessed_set:
            display += letter.upper() + " "
        elif letter == " ":
            display += "  "   # Preserve spaces in multi-word countries
        else:
            display += "_ "

    print(f"Current Word: {display.strip()}")
    return display.strip()