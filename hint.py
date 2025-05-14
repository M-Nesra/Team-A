import random

def get_hint(country):
    """
    Steven Zheng
    
    Technique Used:
        f-strings
        
    Prompts the user to choose a hint type, then returns either:
        First letter
        Last letter
        A random letter in the middle (not first or last)

    Args:
        country (str): The country name

    Returns:
        str: The hint
    """
    print("\n Which hint would you like to use?")
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

def letter_freq(country):
    """
    Steven Zheng
    
    Technique Used:
        f-string
        key function
        
    Returns the most frequently used letter in the country name.
    
    Args:
        country (str): The name of the country.
        
    Returns:
        str: The most frequently appearing letter in the country name.
    """
    freq = {}
    for char in country.lower():
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1

    if not freq:
        return "No alphabetic letters found."

    most_common_letter = max(freq, key=lambda k: freq[k])

    return f"Hint: The most frequently used letter is '{most_common_letter.upper()}'."

def word_structure(country):
    """
    Steven Zheng
    
    Technique Used:
        F-strings
    
    Returns the number of words in the country name and the length of each word.
    
    Args:
        country (str): The name of the country.
        
    Returns:
        str: The number of words in the country name and the
        number of letters per word. 
    """
    words = country.strip().split()
    word_lengths = [len(word) for word in words]

    return (
        f"Hint: The country name has {len(words)} word(s), "
        f"with lengths: {', '.join(str(length) for length in word_lengths)}."
    )