def display_word_state(country,guessed_letters):
    display = ''
    for letter in country:
        if letter.lower() in guessed_letters:
            display += letter + ' '
        elif letter == ' ':
            display += '  ' #add two spaces for multi word countries.
        else:
            display += '_ '

return display.strip()

def pick_country(choice):
    """
       Selects a country based on user input by validating the category, 
       reading from a file, filtering by name length, and picking the one
       with the most unique letters.
        
        Parameters:
         choice (str): Category number as a string ("1" to "4").

        Returns:
         str: The selected country name.
    """

    # Maps menu choice to file name
    CATEGORY_MAP = {
        "1": ("random.txt", "Random Countries"),
        "2": ("africa.txt", "African Countries"),
        "3": ("red_flag.txt", "Countries with Red Flags"),
        "4": ("five_letter.txt", "5-Letter Countries")
    }

    # Check if the input is valid. If not, ask one more time.
    if choice not in CATEGORY_MAP:
        print("Invalid choice. Try one more time.")
        retry = input("Enter the number again: ")
        if retry in CATEGORY_MAP:
            choice = retry
        else:
            print("Still invalid. Defaulting to Random Countries.")
            choice = "1"

    # Get the file name and category label based on input
    file_name, label = CATEGORY_MAP[choice]
    print(f"You picked: {label}")

    # Read country names into a list
    try:
        with open(file_name, "r") as f:
            country_list = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        country_list = []

    # Filter countries that are 5 to 10 characters long
    filtered = [c for c in country_list if 5 <= len(c) <= 10]

    # Sort the list by how many unique letters are in each country name
    filtered.sort(key=mock_unique_score, reverse=True)

    # Pick the top country from list and return
    selected = filtered[0]
    return selected


#Hans
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
 
    if score <= 0:
        print(f"You’ve run out of points. The country was: {country}")
        return guessed_letters, wrong_guesses, score

    return guessed_letters, wrong_guesses, score


# Counts unique letters in a name
def mock_unique_score(name):
    """
    Mock function to simulate scoring based on uniqueness.
    """
    return 5 

if __name__ == "__main__":
    print("Choose a category:")
    print("1. Random Countries")
    print("2. African Countries")
    print("3. Countries with Red Flags")
    print("4. 5-Letter Countries")

    user_input = input("\nEnter the number of your choice: ")
    selected = pick_country(user_input)
