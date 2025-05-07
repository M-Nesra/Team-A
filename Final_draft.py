CATEGORY_MAP = {
    "1": ("random.txt", "Random Countries"),
    "2": ("africa.txt", "African Countries"),
    "3": ("red_flag.txt", "Countries with Red Flags"),
    "4": ("five_letter.txt", "5-Letter Countries")
}

# Loads countries from a file
def load_list(file_name):
    try:
        with open(file_name, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return []

# Loads already used countries
def load_used(file_name="used.txt"):
    try:
        with open(file_name, "r") as f:
            return set(line.strip() for line in f if line.strip())
    except FileNotFoundError:
        return set()

# Saves a country to the used list
def save_used(country, file_name="used.txt"):
    with open(file_name, "a") as f:
        f.write(country + "\n")

# Counts unique letters in a name
def unique_score(name):
    return len(set(name.lower()))

# Checks if input is valid (one retry)
def valid_choice(choice):
    if choice in CATEGORY_MAP:
        return choice

    print("Invalid choice. Try one more time.")
    retry = input("Enter the number again: ")

    if retry in CATEGORY_MAP:
        return retry

    print("\nStill invalid. Defaulting to Random Countries.")
    return "1"

# Picks a country from the chosen category
def pick_country(choice):
    choice = valid_choice(choice)
    file_name, label = CATEGORY_MAP[choice]

    print(f"You picked: {label}")

    # Load and filter countries
    country_list = load_list(file_name)
    filtered = [c for c in country_list if 5 <= len(c) <= 10]

    # Remove ones already used
    used = load_used()
    available = [c for c in filtered if c not in used]

    # If all used, restart the list
    if not available:
        print("All countries used. Starting over.")
        available = filtered

    # Pick the best option and save it
    available.sort(key=unique_score, reverse=True)
    selected = available[0]
    save_used(selected)
    return selected

if __name__ == "__main__":
    print("Choose a category:")
    print("1. Random Countries")
    print("2. African Countries")
    print("3. Countries with Red Flags")
    print("4. 5-Letter Countries")

    user_input = input("\nEnter the number of your choice: ")
    selected = pick_country(user_input)
    
    