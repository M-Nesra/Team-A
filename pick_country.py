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