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


# While there are remaining commands, translate commands to assembely
while parser.hasMoreCommands():
    # Store the current commmand
    command = parser.advance()

    ### Translate the current command to assembley ###
    # If command is push/pop use the writePushPop()  method
    # Else command is arithmetic, use the writeArithmetic() method
    if command[0] == 0:
        generator.writePushPop(command)
    else:
        generator.writeArithmetic(command)
    

# Close the output file
generator.close()

### END ###
