# Woordle: Scoring System

def adjust_score(score: int, type_guess: str, correct_guesses: int = 0):
	“”” This function updates the player's score based on their action.
		Parameters:
            Score (int): the current score of the player.
            Type_guess (str): the type of action for exp: “hint”, “wrong_guess”,
            “bonus”
            Correct_geusses (int) : the amount of correct guesses made, used for 
            bonus

	    Returns:
            The updated score of the player (dependencies, values of parameters 
            listed)
    ”””
    score = 100
    # dictionary for mapping referenced string values to point related actions
    score_changes = {
        “hint”: -15
        “wrong_guess”: -10
        “bonus” = 5 * “correct_guesses” 
    }

    # type guesses are any of the list forms of guessing listed
    if type_guess in score_changes:
        if type_guess == "bonus":
            score += score_changes[type_guess]  
            # bonus is already calculated using correct_guesses
        else:
            score += score_changes[type_guess]
        else:
            print(f"Action isn’t related to the game.")
	
	# leader_board.txt.append(score)  → will add when i create this text file
	return max(score, 0)

