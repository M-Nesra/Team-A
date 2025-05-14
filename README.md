# Team-A

# Geoletter: A Geography Word Challenge
    
    Test your knowledge of world countries in this interactive Python guessing game! Geoletters is a country-themed  word guessing game. You try to guess the letters of a hidden country name before running out of points or guesses

### How to Play:
    1. Pick a category (African nations, countries with red flags, etc.)

    2. Guess letters to reveal the hidden country name

    3. Use hints carefully—they'll cost you points!

    4. Try to solve it quickly for bonus points

### Quick Start:

    bash
    git clone https://github.com/your-repo/Geoletters.git
    cd Geoletters
    python Geoletters.py

### What Makes This Game Unique:
1. Adaptive scoring system that rewards strategic play
2. Multiple difficulty levels through category selection
3. Persistent leaderboard to track top players

### For Other Developers:
    The game uses these key components:

        1. scoring.py handles points and leaderboards

        2. hint_system.py provides intelligent clues

        3. Country data is organized in separate text files

### As we built this, we practiced:

    --> Clean Python architecture
    --> User input validation

# Interpretation of The Program

### Game Rules

    1. You start with 100 points.
    2. You can ake up to 6 wrong guesses. each wrong letter costs 10 points
    3. You can use a hint at any time by typing 'hint' for 15 points:
        a. First letter
        b. Last letter
        c. Random middle letter
        d. Most repetitive leter in the name
        e. word count and word lengths
    4. The game ends when:
        a. You guess all letters in the country
        b. You run out of points
        c. You reach 6 wrong guesses

### Program Ending & Extra Notes

    1. It shows a congratualaitons message if you won, or a game over message with the correct country name
    2. Input is case-insensitive, but with only sinlge alphabetic characters (ex. A, a, B, b)
    3. If all countries in a category have been sued, the list resets
    4. Countries with characters shorter than 5 or longer than 10 will not be displayed
    

# Troubleshooting: 

    If you get stuck:
        --> Make sure all .txt files are in the right folder.
        --> Check you're using an updated Python version.
        --> The game might need permission to update the leaderboard text file.


# Annotated Bibliography:

1. https://wallethub.com/edu/cities-with-the-most-and-least-ethno-racial-and-linguistic-diversity/10264

This documentation provided as a credible source for our elevator pitch. Within the pitch, we were able to describe that Maryland holds four of the most ethnicaly diverse cities in the United States of America. As stated, Germantown was ranked number one as the most ethincally diverse city in the U.S. Next, Gaithesburg was ranked number three as the most ethicnally diverse city in the U.S. Following that, Silver Spring was ranked number four as the the most ethicnally diverse city in the U.S. Finally, Rockville was ranked number nine as the most ethicnally diverse city in the U.S.
    
