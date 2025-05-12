import os
import random
import re

def initialize_score():
    """Initialize the player's score for the start of the Game @ 100"""
    return 100

def adjust_score(score: int, type_guess: str, correct_guesses: int = 0):
    """This function updates the player's score based on their action.

        Parameters:
            --> score (int): the current score of the player.
            --> type_guess (str): the type of action - "hint", "wrong_guess",
            or "bonus")
            --> correct_geusses (int) : the amount of correct guesses made, used
            for bonus

        Returns:
            --> int: This is the updated score of the player (dependencies, values
            provided in parameters)
    """
    
    # Dictionary for mapping referenced string values score changes
    score_changes = {
        "hint": -15,
        "wrong_guess": -10,
        "bonus": 5 if correct_guesses < 3 else 0
    }

    # Condtions that ensure game attempt boundaries:
    if type_guess not in score_changes:
        raise ValueError(f"Action {type_guess} is not viable in this game.")

    score += score_changes[type_guess]

    # Returns score, ensures it does not decrease below 0.
    return max(score, 0)


def update_leaderboard(player_name: str, final_score: int, filename: str = "leader_board.txt"):
    """Updates the leaderboard text file with the player's name and their score.

    Parameters:
        --> player_name (str): the name of the player
        --> final_score (int): the player's final score
        --> filename (str): name of the leaderboard file
    """
    with open(filename, "a") as f:
        f.write(f"{player_name}: {final_score}\n")


def display_leaderboard(filename: str = "leader_board.txt"):
    """ Displays the current leaderboard from the text file designated.

    Parameters:
        filename (str): name of the leaderboard file
    """

    # Isata: I implemented conditional statements here to verfiy the filepath 
    # and display information if the condition is met.
    
    # Checks if the file exists first
    if not os.path.exists(filename):
        print("No leaderboard records yet!")
        return

    # Checks to see if its empty
    if os.path.getsize(filename) == 0:
        print("Leaderboard is empty!")
        return

    # Isata: I utilized with statement to read the file and display current scores:
    with open(filename, "r") as f:
        scores = [line.strip() for line in f if line.strip()]

    # displays distint leaderboard header for better readability
    print("\n--- LEADERBOARD ---")

    # Show last 10 entries (or all if less than 10)
    for score in scores[-10:]:
        print(score)
    print("_____________________")

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
    print("4. Most Common Letter")
    print("5. Word count and word lengths")

    choice = input("Enter 1, 2, 3, 4, or 5: ").strip()
    country_name = country.strip()

    if choice == "1":
        return f"Hint: The first letter of the country is '{country_name[0].upper()}'."
    elif choice == "2":
        return f"Hint: The last letter of the country is '{country_name[-1].upper()}'."
    elif choice == "3":
        middle = list(range(1, len(country_name) - 1))
        random_index = random.choice(middle)
        letter = country_name[random_index]
        return f"Hint: The {random_index + 1}th letter of the country is '{letter.upper()}'."
    elif choice == "4":
        return letter_freq(country_name)
    elif choice == "5":
        return word_structure(country_name)
    else:
        return "Invalid choice. No hint used, but the point deduction still applies."

def letter_freq(country: str) -> str:
    """
    Returns the most frequently used letter in the country name.
    """
    freq = {}
    for char in country.lower():
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1

    if not freq:
        return "No alphabetic letters found."

    most_common_letter = max(freq, key=lambda k: freq[k])

    return f"Hint: The most frequently used letter is '{most_common_letter.upper()}'."

def word_structure(country: str) -> str:
    """
    Returns the number of words in the country name and the length of each word.
    """
    words = country.strip().split()
    word_lengths = [len(word) for word in words]

    return (
        f"Hint: The country name has {len(words)} word(s), "
        f"with lengths: {', '.join(str(length) for length in word_lengths)}."
    )

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

CATEGORY_MAP = {
    "1": ("random.txt", "Random Countries"),
    "2": ("africa.txt", "African Countries"),
    "3": ("red_flag.txt", "Countries with Red Flags"),
    "4": ("five_letter.txt", "5-Letter Countries")
}

# Loads countries from a file
def load_list(file_name):
    try:
        with open(file_name, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return []

# Loads already used countries
def load_used(file_name="used.txt"):
    try:
        with open(file_name, "r") as f:
            return set(line.strip() for line in f if line.strip())
    except FileNotFoundError:
        return set()

# Saves a country to the used list
def save_used(country, file_name="used.txt"):
    with open(file_name, "a") as f:
        f.write(country + "\n")

# Counts unique letters in a name
def unique_score(name):
    return len(set(name.lower()))

# Checks if input is valid (one retry)
def valid_choice(choice):
    if choice in CATEGORY_MAP:
        return choice

    print("Invalid choice. Try one more time.")
    retry = input("Enter the number again: ")

    if retry in CATEGORY_MAP:
        return retry

    print("\nStill invalid. Defaulting to Random Countries.")
    return "1"

# Picks a country from the chosen category
def pick_country(choice):
    choice = valid_choice(choice)
    file_name, label = CATEGORY_MAP[choice]

    print(f"You picked: {label}")

    # Load and filter countries
    country_list = load_list(file_name)
    filtered = [c for c in country_list if 5 <= len(c) <= 10]

    # Remove ones already used
    used = load_used()
    available = [c for c in filtered if c not in used]

    # If all used, restart the list
    if not available:
        print("All countries used. Starting over.")
        available = filtered

    # Pick the best option and save it
    available.sort(key=unique_score, reverse=True)
    selected = available[0]
    save_used(selected)
    return selected

class GameState:
    """
    Represents the state of the guessing game for a single round.

    Attributes:
        country (str): The name of the country to be guessed.
        guessed_letters (set): Set of correctly guessed letters.
        wrong_guesses (int): Number of incorrect guesses.
        score (int): Current player score.
    """
    def __init__(self, country, guessed_letters=None, wrong_guesses=0, score=100):
        """
        Initializes a GameState instance with the provided country and game state info.

        Args:
            country (str): The name of the country to guess.
            guessed_letters (set): Letters guessed so far.
            wrong_guesses (int): Count of incorrect guesses.
            score (int): Starting score.
        """
        self.country = country
        self.guessed_letters = guessed_letters or set()
        self.wrong_guesses = wrong_guesses
        self.score = score

    def __contains__(self, letter):
        """
        Checks whether a letter is in the target country (case-insensitive).

        Args:
            letter (str): The letter to check.

        Returns:
            bool: True if letter is in the country name.
        """
        return letter in self.country.lower()

    def __str__(self):
        """
        Returns the current state of the word with guessed letters revealed.

        Returns:
            str: Display string with correctly guessed letters shown.
        """
        return display_word_state(self.country, self.guessed_letters)


def validate_guess(guess, guessed_letters):
    """
    Validates the format and repetition of the player's guess.

    Args:
        guess (str): The letter guessed by the player.
        guessed_letters (set): Set of letters already guessed.

    Returns:
        tuple: (bool, str) representing whether the guess is valid, and either the cleaned guess or error message.
    """
    guess = guess.strip().lower()

    if not guess.isalpha() or len(guess) != 1:
        return False, "Invalid input. Please guess a single letter."

    if guess in guessed_letters:
        return False, f"You already guessed '{guess.upper()}'."

    return True, guess


def evaluate_guess(guess, state):
    """
    Updates the game state based on the player's guess.

    Args:
        guess (str): The player's guess.
        state (GameState): The current state of the game.

    Returns:
        str: Feedback message on the guess.

    Side effects:
        Updates guessed_letters, wrong_guesses, and score in the state object.
    """
    if guess in state:
        state.guessed_letters.add(guess)
        return f"{state}\n'{guess.upper()}' is correct!"
    else:
        state.wrong_guesses += 1
        state.score = adjust_score(state.score, "wrong_guess")
        return f"'{guess.upper()}' is incorrect. -10 points. Score: {state.score}"


def guess_checker(guess, state):
    """
    Processes the player's guess and updates the game state accordingly.

    Args:
        guess (str): The player's guessed letter.
        state (GameState): The current game state.

    Returns:
        GameState: Updated game state.

    Side effects:
        Prints feedback and possible game end messages.
    """
    is_valid, result = validate_guess(guess, state.guessed_letters)
    if not is_valid:
        print(result)
        return state

    guess = result
    feedback = evaluate_guess(guess, state)

    # Sort messages by their length to control message priority
    messages = [
        (state.wrong_guesses >= 6, f"Game Over. The correct country was: {state.country}"),
        (state.score <= 0, f"You've run out of points. The country was: {state.country}"),
        (True, feedback)
    ]

    for condition, message in sorted(messages, key=lambda x: len(x[1])):
        if condition:
            print(message)
            break

    return state

def play_game():
    

if __name__ == "__main__":
    play_game()
