# This program translates hack-vm code into hack-assembely
# Author: George Duke, Course: Nand to Tetris (ii)


# Import the Parser and Code Generator
import classes.parser
import classes.codeGenerator
import os
from sys import argv

# Store a list of file_names to process
if os.path.isdir(argv[1]):
    # file_names = list of every .vm file in the given directory
    file_names = [os.path.join(argv[1], file) for file in os.listdir(argv[1]) if file[-3:] == '.vm']
else:
    file_names = [argv[1]]  # Input is a single file


for file_name in file_names:
    # Construct the parser and code generator
    parser = classes.parser.Parser(file_name)
    generator = classes.codeGenerator.Generator(file_name)

    while parser.hasMoreCommands():
        semantics = parser.advance()
        # Translate into assembely using the correct method
        if semantics[0] == 0:
            generator.writePushPop(semantics)
        elif semantics[0] == 2:
            generator.writeBranching(semantics)

        else:
            generator.writeArithmetic(semantics)


# Close the output file
generator.close()
