import re
from pathlib import Path

MORSE_CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
              'D': '-..',    'E': '.',      'F': '..-.',
              'G': '--.',    'H': '....',   'I': '..',
              'J': '.---',   'K': '-.-',    'L': '.-..',
              'M': '--',     'N': '-.',     'O': '---',
              'P': '.--.',   'Q': '--.-',   'R': '.-.',
              'S': '...',    'T': '-',      'U': '..-',
              'V': '...-',   'W': '.--',    'X': '-..-',
              'Y': '-.--',   'Z': '--..',

              '0': '-----',  '1': '.----',  '2': '..---',
              '3': '...--',  '4': '....-',  '5': '.....',
              '6': '-....',  '7': '--...',  '8': '---..',
              '9': '----.',

              '.': '.-.-.-', ',': '--..--', ':': '---...',
              "'": '.----.', '-': '-....-',
              }

def english_to_morse(
    input_file: str = "lorem.txt",
    output_file: str = "lorem_morse.txt"
):
    """Convert an input text file to an output Morse code file.

    Notes
    -----
    This function assumes the existence of a MORSE_CODE dictionary, containing a
    mapping between English letters and their corresponding Morse code.

    Parameters
    ----------
    input_file : str
        Path to file containing the text file to convert.
    output_file : str
        Name of output file containing the translated Morse code. Please don't change
        it since it's also hard-coded in the tests file.
    """

    script_location = Path(__file__).parent.resolve()  # full path to this script
    input_path = script_location / input_file
    output_path = script_location / output_file

    with open(input_path, 'r') as f:
        lorem_str = f.read().upper() # Converting everything to capital since our dictionary is for uppercase characters

    new_str = re.sub(r'[A-Z0-9\.\,\:\'\-]', lambda m: MORSE_CODE[m.group()], lorem_str) # avoiding a loop with a lambda
    new_str = new_str.replace(' ', '\n')
    
    with open(output_path, 'w') as f:
        f.write(new_str)

if __name__ == "__main__":
    english_to_morse()
