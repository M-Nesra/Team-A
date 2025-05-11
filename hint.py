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
        middle_indices = list(range(1, len(country_name) - 1))
        random_index = random.choice(middle_indices)
        letter = country_name[random_index]
        return f"Hint: The {random_index + 1}ᵗʰ letter of the country is '{letter.upper()}'."
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