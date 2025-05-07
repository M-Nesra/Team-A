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

import random

def get_hint(country: str):
    """
    Prompts the user to choose a hint type, then returns either:
        First letter
        Last letter
        A random letter in the middle (not first or last)

    Parameters:
        country (str): The country name

    Returns:
        str: The hint
    """
    print("\nWhich hint would you like to use?")
    print("1. First Letter")
    print("2. Last Letter")
    print("3. Random Letter in Between (not first or last)")

    choice = input("Enter 1, 2, or 3: ").strip()

    country_name = country.strip()

    if choice == "1":
        return f"Hint: The first letter of the country is '{country_name[0].upper()}'."
    elif choice == "2":
        return f"Hint: The last letter of the country is '{country_name[-1].upper()}'."
    elif choice == "3":
        if len(country_name) <= 2:
            return "Hint: The country name is too short for a middle letter hint."
        middle_indices = list(range(1, len(country_name) - 1))
        random_index = random.choice(middle_indices)
        letter = country_name[random_index]
        return f"Hint: The {random_index + 1}ᵗʰ letter of the country is '{letter.upper()}'."
    else:
        return "Invalid choice. No hint used, but the point deduction still applies."
    
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

# Woordle: Scoring System

def adjust_score(score: int, type_guess: str, correct_guesses: int = 0):
        """ This function updates the player's score based on their action.
            Parameters:
                Score (int): the current score of the player.
                Type_guess (str): the type of action for exp: “hint”, “wrong_guess”,
                “bonus”
                Correct_geusses (int) : the amount of correct guesses made, used for 
                bonus

            Returns:
                The updated score of the player (dependencies, values of parameters 
                listed)
        """
        
        score = 100
    # dictionary for mapping referenced string values to point related actions
        score_changes = {
             “hint”: -15
                “wrong_guess”: -10
                “bonus” = 5 * “correct_guesses” }

    # type guesses are any of the list forms of guessing listed
    if type_guess in score_changes:
        if type_guess == "bonus":
            score += score_changes[type_guess]  
            # bonus is already calculated using correct_guesses
        else if:
            score += score_changes[type_guess]
        else:
            print(f"Action isn’t related to the game.")
	
	# leader_board.txt.append(score)  → will add when i create this text file
	    return max(score, 0)
