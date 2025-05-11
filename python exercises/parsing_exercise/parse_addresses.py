from argparse import ArgumentParser
import re
import sys

class Address:
    """
    Represents a US street address with parsed components.
    
    Attributes:
        address (str): The full address string.
        house_number (str): The house number of the address.
        street (str): The street name.
        city (str): The city name.
        state (str): The two-letter state abbreviation.
        zip (str): The five-digit ZIP code.
    """
    
    def __init__(self, address: str):
        """
        Initializes an Address object by parsing the given address string.
        
        Args:
            address (str): The full address as a string.
        
        Side effects:
            Initializes the instance attributes: address, house_number, street, 
            city, state, and zip.
        
        Raises:
            ValueError: If the address string cannot be parsed.
        """
        self.address = address.strip()
        
        # Regular expression pattern for parsing the address
        pattern = re.compile(r'^(\S+)\s+(.*?),\s+(.*?)\s+([A-Z]{2})\s+(\d{5})$')
        match = pattern.search(self.address)
        
        if not match:
            raise ValueError(f"Address could not be parsed: {address}")
        
        self.house_number = match.group(1)
        self.street = match.group(2)
        self.city = match.group(3)
        self.state = match.group(4)
        self.zip = match.group(5)

    def __repr__(self):
        """
        Returns a formal representation of the Address object.
        
        Returns:
            str: A formatted string representation of the Address object.
        """
        return (
            f"address:      {self.address}\n"
            f"house number: {self.house_number}\n"
            f"street:       {self.street}\n"
            f"city:         {self.city}\n"
            f"state:        {self.state}\n"
            f"zip:          {self.zip}"
        )

def read_addresses(file_path: str):
    """
    Reads addresses from a file and returns a list of Address objects.
    
    Args:
        file_path (str): The path to the file containing one address per line.
    
    Returns:
        list: A list of Address objects parsed from the file.
    """
    with open(file_path, 'r') as file:
        return [Address(line) for line in file if line.strip()]

def parse_args(arglist):
    """
    Parse command-line arguments.
    
    Expect one mandatory argument, the path to a file of addresses.
    
    Args:
        arglist (list of str): Command-line arguments.
    
    Returns:
        namespace: An object with one attribute, file, containing a string.
    """
    parser = ArgumentParser()
    parser.add_argument("file", help="file containing one address per line")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    for address in read_addresses(args.file):
        print(f"{address!r}\n")
