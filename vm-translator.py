# This program translates hack-vm code into hack-assembely
# Author: George Duke, Course: Nand to Tetris (ii)


# Import the Parser and Code Generator
import classes.parser
import classes.codeGenerator

# Import argv from sys (extract command line argument of file)
from sys import argv

# Get Directory/Filename from CLI
file_name = argv[1]

# Construct the parser and code generator
parser = classes.parser.Parser(file_name)
generator = classes.codeGenerator.Generator(file_name)


while parser.hasMoreCommands():
    semantics = parser.advance()
    # Translate into assembely using the correct method
    if semantics[0] == 0:
        generator.writePushPop(semantics)
    else:
        generator.writeArithmetic(semantics)
    

# Close the output file
generator.close()
