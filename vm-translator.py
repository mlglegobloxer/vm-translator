# This program translates hack-vm code into hack-assembely
# Author: George Duke, Course: Nand to Tetris (ii)

# Requred imports
import classes.parser
import classes.codeGenerator
import os
from sys import argv


# Store a list of input_file_names to process
if os.path.isdir(argv[1]):
    input_file_names = [os.path.join(argv[1], file) for file in os.listdir(argv[1]) if file[-3:] == '.vm'] # All .vm files in directory
    output_file_name = str(argv[1])[0:-1] + ".asm" # Output file name <- inputdirname.asm
else:
    input_file_names = [argv[1]] # Input is a single file
    output_file_name = str(argv[1])[0:-3] + ".asm" # Output file name <- inputfilename.asm


# Create the code generator for the output file
generator = classes.codeGenerator.Generator(output_file_name)

# Compile all input files
for file_name in input_file_names:
    # Construct the parser for the file
    parser    = classes.parser.Parser(file_name)
    # Compile each line
    while parser.hasMoreCommands():
        semantics = parser.advance()
        # Translate into assembely using the correct method
        if   semantics[0] == 0: generator.writePushPop(semantics)
        elif semantics[0] == 1: generator.writeArithmetic(semantics)
        elif semantics[0] == 2: generator.writeBranching(semantics)
        elif semantics[0] == 3: generator.writeFunction(semantics)
        elif semantics[0] == 3: generator.writeCall(semantics)
        elif semantics[0] == 3: generator.writeReturn(semantics)

    # Close the output file

generator.close()
