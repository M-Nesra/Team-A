def get_hint(country_data: dict) -> str:
    """
    Prompts the user to select a hint type and returns the corresponding hint.

    Parameters:
        country_data (dict): Dictionary containing country info like:
        {
            "name": "Nigeria",
            "continent": "Africa",
            "flag_colors": "Green, White, Green",
            "first_letter": "N"
        }

    Returns:
    - str: Hint string to display.
    """
    print("\nSelect the type of hiint:")
    print("1. Continent")
    print("2. Flag Colors")
    print("3. First Letter")

    hint_choice = input("Enter 1, 2, or 3: ").strip()

    if hint_choice == "1":
        return f"Hint: The country is in {country_data['continent']}."
    elif hint_choice == "2":
        return f"Hint: The country's flag contains the colors: {country_data['flag_colors']}."
    elif hint_choice == "3":
        return f"Hint: The country starts with the letter '{country_data['first_letter']}'."
    else:
        return "Invalid choice. No hint used."
