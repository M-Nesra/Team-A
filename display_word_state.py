import re

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


def valid_country_format(country_name):
    """
    Validates the format of a country name using a regular expression.

    A valid country name contains only letters and spaces (no digits, punctuation, etc.).

    Args:
        country_name: The user input country name to validate.

    Returns:
        True if the format is valid, False otherwise.
    """
    country_name = country_name.strip()
    pattern = re.compile(r"^[A-Za-z ]+$")  # Only letters and spaces allowed

    # Checks if the entire string matches the pattern
    match = re.search(pattern, country_name)
    
    #Verifies that the match spans the full string
    is_valid = match is not None and match.group() == country_name

    print(f"Validation Result for '{country_name}': {'Valid' if is_valid else 'Invalid'}")
    return is_valid
