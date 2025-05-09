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
