# This program implements a parser class for the vm translator
# Author: George Duke, Course: Nand to Tetris (ii)

class Parser:
    # Constructor method: read input file, initialise object
    def __init__(self, file_name):
        # Read the input file
        input_file = open(file_name, "r")

        # Define self.lines as the list of all lines in the input_file (removing \n)
        self.lines = [line.rstrip() for line in input_file.readlines()]

        # Remove lines that are comments or empty
        self.lines = [line for line in self.lines if ("/" not in line) and (line != "")]

        # Reverse the list so the advance() method may use pop() to remove parsed lines
        self.lines.reverse()
 
        # Close the input file
        input_file.close()


    def hasMoreCommands(self):
        # Returns True if any more commands to be read (boolean) #
        return(self.lines != [])


    def advance(self):
        # Reads the current command, removes self.lines, returns its semantics #

        # Pop the current line of the remaining lines and store in current_line
        current_line = self.lines.pop()

        # Extract the command's semantics in the form: [command<str>] or [command<str>, segment<str>, index<index>]
        semantics = current_line.split()

        # Encode the command's type (0 => push/pop, 1 => arithmetic/logic, 2 => branching, 3 => function)
        if semantics[0] in ["push", "pop"]:
            semantics = [0] + semantics         # Add 0 to the start of the list
            semantics[-1] = int(semantics[-1])  # Convert index from <str> to <int>
        else:
            semantics = [1] + semantics         # Add 1 to the start of the list

        # Return the semantics in the form:
        # For Push / Pop : [type(0), command<str>, segment<str>, index<index>]
        # For Arithmetic : [type(1), command<str>]
        return(semantics)
