from argparse import ArgumentParser
import sys


def evaluate(expression):
    """
    Evaluates a postfix (reverse Polish notation) mathematical expression.

    Args:
        expression: A space-separated string representing a postfix expression.

    Returns:
        float: The evaluated result of the postfix expression.
    """
    number = []  # Stack to store numbers
    elements = expression.strip().split()  # Split expression into elements
    
    for element in elements:
        if element in ['+', '-', '*', '/']:
            # Pop two numbers from number_stack
            num2 = number.pop()
            num1 = number.pop()
            
            # Perform the operation
            if element == '+':
                result = num1 + num2
            elif element == '-':
                result = num1 - num2
            elif element == '*':
                result = num1 * num2
            elif element == '/':
                result = num1 / num2
            
            # Push result back onto number
            number.append(result)
        else:
            # Convert number from string to float and push onto number
            number.append(float(element))
    
    return number.pop()  # Final result

def main(filename):
    """
    Reads a file containing postfix expressions and evaluates each expression.

    Args:
        filename : The path to the file containing postfix expressions.
    
    Side effects:
        Prints the result of each evaluated postfix expression.
    """
    try:
        with open(filename, 'r') as file:
            for line in file:
                expression = line.strip() # Remove any leading/trailing space
                if expression:
                    result = evaluate(expression)
                    print(f"{expression} = {result}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def parse_args(arglist):
    """ Process command line arguments.
    
    Expect one mandatory argument (a file containing postfix expressions).
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("file", help="file containing reverse polish notation")
    args = parser.parse_args(arglist)
    return args


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)
