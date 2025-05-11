"""
Do: Determine the relationship between two individuals in a family based on JSON data.
"""

import argparse
import json
import sys
from relationships import relationships


class Person:
    """
    Represents an individual with attributes: name, gender, parents, and spouse.

    Attributes:
        name (str): The person's name.
        gender (str): The person's gender.
        parents (list[Person]): List of parent objects.
        spouse (Person): The person's spouse.
    """

    def __init__(self, name, gender):
        """
        Initialize a Person with name, gender, empty parents list, and no spouse.

        Args:
            name (str): The name of the person.
            gender (str): The gender of the person.

        Side effects:
            - Creates an instance of Person.
            - Initializes empty parents list and sets spouse to None.
        """
        self.name = name
        self.gender = gender
        self.parents = []
        self.spouse = None

    def add_parent(self, parent):
        """
        Add a parent to the person's parents list.

        Args:
            parent (Person): The parent to add.

        Side effects:
            - Modifies the `parents` list by appending a new parent.
        """
        self.parents.append(parent)

    def set_spouse(self, spouse):
        """
        Set the person's spouse.

        Args:
            spouse (Person): The spouse to assign.

        Side effects:
            - Assigns a spouse to the Person instance.
        """
        self.spouse = spouse

    def connections(self):
        """
        Find all relatives connected through parents and/or spouse.

        Returns:
            dict: A dictionary mapping related Person instances to relationship paths.
        
        Example:
            >>> person.connections()
            {<Person object>: "P", <Person object>: "S"}
        """
        cdict = {self: ""}
        queue = [self]

        while queue:
            person = queue.pop(0)
            personpath = cdict[person]

            for parent in person.parents:
                if parent not in cdict:
                    cdict[parent] = personpath + "P"
                    queue.append(parent)

            if ("S" not in personpath and person.spouse and
                    person.spouse not in cdict):
                cdict[person.spouse] = personpath + "S"
                queue.append(person.spouse)

        return cdict

    def relation_to(self, other):
        """
        Determine the relationship to another person.

        Args:
            other (Person): The person to find the relationship with.

        Returns:
            str: The relationship description or "distant relative" if not defined.

        Example:
            >>> person1.relation_to(person2)
            'cousin'
        """
        connections_self = self.connections()
        connections_other = other.connections()

        shared = set(connections_self.keys()) & set(connections_other.keys())
        if not shared:
            return None

        combined_paths = {
            connections_self[rel] + ":" + connections_other[rel]
            for rel in shared
        }

        lcr_path = min(combined_paths, key=len)

        if lcr_path in relationships:
            return relationships[lcr_path].get(self.gender, "distant relative")

        return "distant relative"


class Family:
    """
    Represents a family composed of multiple Person instances.

    Attributes:
        people (dict): A dictionary mapping names to Person instances.
    """

    def __init__(self, family_data):
        """
        Initialize the family with people, parents, and couples.

        Args:
            family_data (dict): JSON dictionary with individuals, parents, and couples.

        Side effects:
            - Creates Person instances for each individual in the data.
            - Establishes parent-child and spouse relationships.
        """
        self.people = {}

        for name, gender in family_data["individuals"].items():
            self.people[name] = Person(name, gender)

        for child, parents in family_data["parents"].items():
            for parent in parents:
                self.people[child].add_parent(self.people[parent])

        for spouse1, spouse2 in family_data["couples"]:
            self.people[spouse1].set_spouse(self.people[spouse2])
            self.people[spouse2].set_spouse(self.people[spouse1])

    def relation(self, name1, name2):
        """
        Find the relation between two people.

        Args:
            name1 (str): The first person's name.
            name2 (str): The second person's name.

        Returns:
            str: The relationship description or None if no relation exists.

        Example:
            >>> family.relation("Alice", "Bob")
            'cousin'
        """
        person1 = self.people[name1]
        person2 = self.people[name2]
        return person1.relation_to(person2)


def main(filepath, name1, name2):
        """
        Main function to read JSON file, create Family instance, and find relation.

        Args:
            filepath (str): Path to the family JSON file.
            name1 (str): Name of the first person.
            name2 (str): Name of the second person.

        Side effects:
            - Reads and loads the JSON file.
            - Creates a Family instance.
            - Prints the relationship or a message if unrelated.
        """
        with open(filepath, "r", encoding="utf-8") as f:
            family_data = json.load(f)

        family = Family(family_data)

        relation = family.relation(name1, name2)

        if relation is None:
            print(f"{name1} is not related to {name2}")
        else:
            print(f"{name1} is {name2}'s {relation}")


def parse_args(args):
    """
    Parse command-line arguments.

    Args:
        args (list): List of command-line arguments.

    Returns:
        argparse.Namespace: Parsed arguments containing:
            - filepath (str): The family JSON file path.
            - name1 (str): First person's name.
            - name2 (str): Second person's name.
        
    Example:
        >>> parse_args(["family.json", "Alice", "Bob"])
        Namespace(filepath='family.json', name1='Alice', name2='Bob')
    """
    parser = argparse.ArgumentParser(
        description="Find the relationship between two people in a family."
    )

    parser.add_argument("filepath", help="Path to the family JSON file.")
    parser.add_argument("name1", help="First person's name.")
    parser.add_argument("name2", help="Second person's name.")
    
    return parser.parse_args(args)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filepath, args.name1, args.name2)

