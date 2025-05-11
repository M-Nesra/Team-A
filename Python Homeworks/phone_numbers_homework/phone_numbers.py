from argparse import ArgumentParser
import re
import sys


LETTER_TO_NUMBER = {
    'A': '2',
    'B': '2',
    'C': '2',
    'D': '3',
    'E': '3',
    'F': '3',
    'G': '4',
    'H': '4',
    'I': '4',
    'J': '5',
    'K': '5',
    'L': '5',
    'M': '6',
    'N': '6',
    'O': '6',
    'P': '7',
    'Q': '7',
    'R': '7',
    'S': '7',
    'T': '8',
    'U': '8',
    'V': '8',
    'W': '9',
    'X': '9',
    'Y': '9',
    'Z': '9'
}

class PhoneNumber:
    """
    A class to represent and validate a US phone number.

    This class processes and stores a phone number in a standardized format.
    It handles alphanumeric input (e.g., 1-800-FLOWERS), strips the country 
    code if present, replaces letters with corresponding digits, and validates 
    the structure of the number.

    Attributes:
        area_code (str): The 3-digit area code.
        exchange_code (str): The 3-digit exchange code.
        line_number (str): The 4-digit line number.

    Methods:
        __init__(number): Parses and validates the input phone number.
        __str__(): Returns formatted string representation.
        __repr__(): Returns unambiguous representation of the object.
        __int__(): Returns integer representation of the phone number.
        __lt__(other): Compares two phone numbers by integer value.
    """
    
    def __init__(self, number):
        """
        Parses and validates a phone number input.

        Converts an alphanumeric phone number into a standardized numeric format.
        Removes country code if present, replaces letters with digits, and ensures
        the phone number is valid under North American rules.

        Args:
            number (str or int): The input phone number.

        Raises:
            TypeError: If the input is not a string or integer.
            ValueError: If the phone number does not contain exactly 10 digits 
                        after removing the country code, or if it contains 
                        invalid area or exchange codes.

        Side effects:
            Modifies the instance by setting area_code, exchange_code, and 
            line_number attributes.
        """
        if not isinstance(number, (str, int)):
            raise TypeError("Must be a string or integer")

        num_str = str(number).upper()
        num_str = re.sub(r'[A-Z]', lambda m: LETTER_TO_NUMBER[m.group()], num_str)
        digits = re.sub(r'\D', '', num_str)

        if digits.startswith('1'):
            digits = digits[1:]

        if len(digits) != 10:
            raise ValueError(
                "Must contain exactly 10 digits after country code removal")

        area, exchange, line = digits[:3], digits[3:6], digits[6:]

        if (area[0] in "01" or exchange[0] in "01" or
                area.endswith("11") or exchange.endswith("11")):
            raise ValueError("Invalid area or exchange code")

        self.area_code = area
        self.exchange_code = exchange
        self.line_number = line

    def __str__(self):
        """Returns the phone number in (XXX) XXX-XXXX format."""
        return f"({self.area_code}) {self.exchange_code}-{self.line_number}"

    def __repr__(self):
        """Returns the string representation used to recreate the object."""
        return (
            f"PhoneNumber('{self.area_code}"
            f"{self.exchange_code}{self.line_number}')"
        )

    def __int__(self):
        """Returns the phone number as an integer."""
        return int(self.area_code + self.exchange_code + self.line_number)

    def __lt__(self, other):
        """Compares two PhoneNumber instances by their integer values."""
        if not isinstance(other, PhoneNumber):
            return NotImplemented
        return int(self) < int(other)


def read_numbers(path):
    """
    Reads a file and returns a sorted list of (name, PhoneNumber) tuples.

    Args:
        path (str): Path to a UTF-8 encoded file.

    Returns:
        List[Tuple[str, PhoneNumber]]: Sorted by phone number.
    """
    result = []
    with open(path, encoding="utf-8") as file:
        for line in file:
            try:
                name, number = line.strip().split('\t')
                phone = PhoneNumber(number)
                result.append((name, phone))
            except (ValueError, TypeError):
                print(
                    f"Skipping malformed line: {line.strip()}",
                    file=sys.stderr
                )

    return sorted(result, key=lambda pair: pair[1])

def main(path):
    """Read data from path and print results.
    
    Args:
        path (str): path to a text file. Each line in the file should consist of
            a name, a tab character, and a phone number.
    
    Side effects:
        Writes to stdout.
    """
    for name, number in read_numbers(path):
        print(f"{number}\t{name}")


def parse_args(arglist):
    """Parse command-line arguments.
    
    Expects one mandatory command-line argument: a path to a text file where
    each line consists of a name, a tab character, and a phone number.
    
    Args:
        arglist (list of str): a list of command-line arguments to parse.
        
    Returns:
        argparse.Namespace: a namespace object with a file attribute whose value
        is a path to a text file as described above.
    """
    parser = ArgumentParser()
    parser.add_argument("file", help="file of names and numbers")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)
