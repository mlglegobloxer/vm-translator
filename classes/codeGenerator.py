# This program implements a code generator class for the vm translator
# Author: George Duke, Course: Nand to Tetris (ii)

# Import regex character substitution and the command dictionaries
from re import sub
from classes.commandDictionaries import *

class Generator:
    def __init__(self, file_name):
        self.file_name = file_name[0:-3] + ".asm" # Change extention from .vm to .asm
        self.output_file = open(self.file_name, "w")

        # Define the command dictonaries for all command types
        self.AL_command_dictionary = AL_command_dictionary
        self.PP_command_dictionary = PP_command_dictionary
        
        # Define a varible used to generate unique labels for commands that require them 
        self.i = 0

        # Set the stack pointer to 256
        self.output_file.writelines('\n'.join(["// Set SP to 256", "@256", "D=A", "@SP", "M=D"]) + "\n")
        # Does this need to be done for local, argument, this and that???
        

    def writeArithmetic(self, semantics):
        # Writes arithmetic / logic commands to output file, given the commands semantics #
        # Write the original command commented out (for debugging)
        self.output_file.writelines("// " + ' '.join(str(item) for item in semantics[1:]) + "\n")
        # Generate assembly from the AL comm. dict.
        assembely = self.AL_command_dictionary[semantics[1]] 
        # For commands that need to create unique labels, use i to do so
        if semantics[1] in ["eq", "gt", "lt"]:
            assembely = [sub("i", str(self.i), command) for command in assembely]
            self.i += 1
        # Write the assembely to the output file
        self.output_file.writelines('\n'.join(assembely) + "\n")


    def __specialPushPopRegex__(self, semantics, assembely):
        ### Special Command Processing For: static, temp, pointer. Used by the writePushPop() method, implemented for modularity ###
        # For commmands using static replace # with the file_name.index
        if semantics[2] == "static":
            return([sub("#", str(self.file_name[0:-3]) + str(semantics[3]), command) for command in assembely])
        # For commmands using temp replace # with the 4 + index
        elif semantics[2] == "temp":
            return([sub("#", str(4 + semantics[3]), command) for command in assembely])
        # For commmands using pointer replace # with: THIS, (index = 0) or THAT, (index = 1)
        elif semantics[2] == "pointer":
            this_that = "THIS" if semantics[3] == 0 else "THAT"
            return([sub("#", this_that, command) for command in assembely])
        # For non special commands, do nothing
        else:   
            return(assembely)


    def writePushPop(self, semantics):
        # Writes push / pop commands to output file, given the commands semantics #
        # Write the original command commented out (for debugging)
        self.output_file.writelines("// " + ' '.join(str(item) for item in semantics[1:]) + "\n")
        # Assembely generation
        assembely = self.PP_command_dictionary[semantics[2] + " " + semantics[1]] # Lookup command in the PP comm. dict.
        assembely = [sub("\*", str(semantics[3]), command) for command in assembely] # Replace placeholder * with the index of the specific command using regex
        assembely = self.__specialPushPopRegex__(semantics, assembely) # Process special commands
        # Write the assembely to the output
        self.output_file.writelines('\n'.join(assembely) + "\n") 


    def close(self):
        self.output_file.close()
