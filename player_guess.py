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