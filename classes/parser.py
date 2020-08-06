# This program implements a parser class for the vm translator
# Author: George Duke, Course: Nand to Tetris (ii)

import re

class Parser:
    # Constructor method: read input file, initialise object
    def __init__(self, file_name):
        input_file = open(file_name, "r")

        # Define self.lines as the list of all lines in the input_file (removing \n, then comments or empty space)
        self.lines = [line.rstrip() for line in input_file.readlines()]
        self.lines = [re.sub(re.compile("//.*$"), "", line) for line in self.lines] # Remove comments
        self.lines = [line for line in self.lines if (line != "")] # Remove empty lines
        self.lines.reverse() # So the advance() method may use pop() to remove parsed lines

        input_file.close()


    def hasMoreCommands(self):
        return(self.lines != [])


    def advance(self):
        # Reads the current command, removes it from self.lines, returns its semantics #
        current_line = self.lines.pop()  # Command to be processed
        semantics = current_line.split() # Break into parts

        # Encode the command's type (0 => push/pop, 1 => arithmetic/logic, 2 => branching, 3 => function)
        if semantics[0] in ["push", "pop"]:
            semantics = [0] + semantics         # Add 0 to the start of the list
            semantics[-1] = int(semantics[-1])  # Convert index from <str> to <int>
        
        elif semantics[0] in ["label", "if-goto", "goto"]:
            semantics = [2] + semantics         # Add 2 to the start of the list
        
        elif semantics[0] == "function":
            semantics = [3] + semantics
            semantics[-1] = int(semantics[-1])  # Convert nvar from <str> to <int>

        elif semantics[0] == "call":
            semantics = [4] + semantics
            semantics[-1] = int(semantics[-1])  # Convert nargs from <str> to <int>

        elif semantics[0] == "return":
            semantics = [5] + semantics

        else:
            semantics = [1] + semantics         # Add 1 to the start of the list

        return(semantics)

        # Return the semantics in the form:
        # For Push / Pop : [type(0), command<str>, segment<str>, index<int>]
        # For Arithmetic : [type(1), command<str>]
        # For Branching  : [type(2), command<str>, reference<str>]
        # For Function   : [type(3), command<str>, name<str>, nvars<int>] 
        # For Call       : [type(4), command<str>, name<str>, nargs<int>]
        # For Return     : [type(5), command<str>]