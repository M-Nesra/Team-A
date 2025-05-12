# Scoring System:

import os

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
    # Isata: Key functions are implemented here to return the score of no less
    # than zero of a player.
    
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

    # Reads the file and displays current scores:
    with open(filename, "r") as f:
        scores = [line.strip() for line in f if line.strip()]

    # displays distint leaderboard header for better readability
    print("\n--- LEADERBOARD ---")

    # Show last 10 entries (or all if less than 10)
    for score in scores[-10:]:
        print(score)
    print("_____________________")


# Testing the scoring system:
if __name__ == "__main__":
    # Test initialization
    score = initialize_score()
    print(f"Initial score: {score}")

    # Test hint deduction
    score = adjust_score(score, "hint")
    print(f"Score after hint: {score}")

    # Test bonus with 2 correct guesses
    score = adjust_score(score, "bonus", 2)
    print(f"Score after bonus: {score}")

    # Test leaderboard functions
    update_leaderboard("TestPlayer", score)
    display_leaderboard()
