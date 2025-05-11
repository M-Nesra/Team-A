"""
Convert numbers from digits to words in Estonian.
"""

from argparse import ArgumentParser
import sys

LANGUAGES = ["est"]

def est(number):
    """
    Converts a number to its Estonian spelling.
    
    Args:
        number (int): The number to be spelled out (0 <= number <= 999999).
    
    Returns:
        str: The number spelled out in Estonian.
    """
    ones = ["null", "üks", "kaks", "kolm", "neli", "viis", "kuus", "seitse", 
            "kaheksa", "üheksa"]
    teens = ["kümme", "üksteist", "kaksteist", "kolmteist", "neliteist", 
             "viisteist", "kuusteist", "seitseteist", "kaheksateist", 
             "üheksateist"]
    tens = ["", "", "kakskümmend", "kolmkümmend", "nelikümmend", "viiskümmend", 
            "kuuskümmend", "seitsekümmend", "kaheksakümmend", 
            "üheksakümmend"]
    hundreds = ["", "sada", "kakssada", "kolmsada", "nelisada", "viissada", 
                "kuussada", "seitsesada", "kaheksasada", "üheksasada"]
    
    if number == 0:
        return "null"
    
    result = []
    
    if number >= 1000:
        thousands = number // 1000
        if thousands == 1:
            result.append("tuhat")
        else:
            result.append(est(thousands) + " tuhat")
        number %= 1000
    
    if number >= 100:
        result.append(hundreds[number // 100])
        number %= 100
    
    if number >= 20:
        result.append(tens[number // 10])
        number %= 10
    
    if number >= 10:
        result.append(teens[number - 10])
        number = 0
    
    if number > 0:
        result.append(ones[number])
        
    return " ".join(result).strip()
        
        
def main(language, input_file, output_file):
    """
    Reads numbers from an input file, converts them to their Estonian spelling,
    and writes the results to an output file.
    
    Args:
        language (str): The language code (must be "est").
        input_file (str): Path to the input file.
        output_file (str): Path to the output file.
    
    Side effects:
        Writes output to a file.
    
    Raises:
        ValueError: If the language is not "est".
    """
    if language != "est":
        raise ValueError("This program only accepts Estonian (est).")
    
    with open(input_file, "r", encoding="utf-8") as file_in, open(output_file, 
              "w", encoding="utf-8") as file_out:
        for line in file_in:
            number = int(line.strip())
            spelled_out = est(number)
            file_out.write(f"{number} = {spelled_out}\n")

def parse_args(arglist):
    """Parse command-line arguments.
    
    Three arguments are required, in the following order:
    
        lang (str): the ISO 639-3 language code of the language the user wants
            to convert numbers into.
        input_file (str): path to a file containing numbers expressed as digits.
        output_file (str): path to a file where numbers will be written as words
            in the target language.

    Args:
        arglist (list of str): list of command-line arguments.

    Returns:
        namespace: the parsed arguments as a namespace. The following 
        attributes will be defined: lang, input_file, and output_file. See 
        above for details.
    """
    parser = ArgumentParser()
    parser.add_argument("lang", help="ISO 639-3 language code")
    parser.add_argument("input_file", help="input file containing numbers")
    parser.add_argument("output_file", help="file where output will be stored")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.lang, args.input_file, args.output_file)
