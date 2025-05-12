import random

class Hint:
    def __init__(self, country):
        self.country = country.strip()

    def get_hint(self):
        print("\nWhich hint would you like to use?")
        print("1. First Letter")
        print("2. Last Letter")
        print("3. Random Letter in Between (not first or last)")
        print("4. Most Common Letter")
        print("5. Word count and word lengths")

        choice = input("Enter 1, 2, 3, 4, or 5: ").strip()

        if choice == "1":
            return f"Hint: The first letter of the country is '{self.country[0].upper()}'."
        elif choice == "2":
            return f"Hint: The last letter of the country is '{self.country[-1].upper()}'."
        elif choice == "3":
            middle = list(range(1, len(self.country) - 1))
            random_index = random.choice(middle)
            letter = self.country[random_index]
            return f"Hint: The {random_index + 1}th letter of the country is '{letter.upper()}'."
        elif choice == "4":
            return self.letter_freq()
        elif choice == "5":
            return self.word_structure()
        else:
            return "Invalid choice. No hint used, but the point deduction still applies."

    def letter_freq(self):
        freq = {}
        for char in self.country.lower():
            if char.isalpha():
                freq[char] = freq.get(char, 0) + 1

        if not freq:
            return "No alphabetic letters found."

        most_common_letter = max(freq, key=lambda k: freq[k])
        return f"Hint: The most frequently used letter is '{most_common_letter.upper()}'."

    def word_structure(self):
        words = self.country.split()
        word_lengths = [len(word) for word in words]

        return (
            f"Hint: The country name has {len(words)} word(s), "
            f"with lengths: {', '.join(str(length) for length in word_lengths)}."
        )