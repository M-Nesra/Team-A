"""Compute a team's score for a (fictitious) word game.

In this game, two players independently find words in a matrix of letters.
Each player's words are added to a text file with one word per line. Duplicates
are removed from each player's list. For each word that appears on both players'
lists, the team's score increases by the number of letters in the word minus 2
(words less than three characters long are not worth any points).
"""


from argparse import ArgumentParser
import sys

class PlayerWords:
    """
    Represents a player's unique words found in the game.
    
    Attributes:
        words (set): A set of unique words found by the player.
    """
    
    def __init__(self, file_path):
        """
        Initializes PlayerWords with words from a file.
        
        Args:
            file_path (str): Path to the text file containing words.
        """
        with open(file_path, 'r') as file:
            self.words = {line.strip() for line in file}

    def score(self, partner):
        """
        Computes the team's score based on shared words.
        
        Args:
            partner (PlayerWords): The partner's words.
        
        Returns:
            int: Total score from common words of length >= 3.
        """
        return sum(len(word) - 2 for word in (self.words & partner.words) 
                   if len(word) >= 3)

def main(player1_file, player2_file):
    """
    Reads words from files, computes, and prints the score.
    
    Args:
        player1_file (str): Path to player 1's word file.
        player2_file (str): Path to player 2's word file.
    
    Side effects:
        Prints the team's score.
    """
    player1 = PlayerWords(player1_file)
    player2 = PlayerWords(player2_file)
    print(f"Your team scored {player1.score(player2)} points!")





def parse_args(arglist):
    """Parse command line arguments.
    
    Expect two mandatory arguments:
        - str: path to a text file containing words found by player 1.
        - str: path to a text file containing words found by player 2.
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.

    """
    parser = ArgumentParser()
    parser.add_argument("wordfile1", help="file containing player 1's words")
    parser.add_argument("wordfile2", help="file containing player 2's words")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.wordfile1, args.wordfile2)
