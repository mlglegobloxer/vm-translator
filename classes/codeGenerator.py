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

        # Set the initial state of the stack machine
        self.output_file.writelines('\n'.join(Init_command_list) + "\n")
        
        
    def writeArithmetic(self, semantics):
        """ Writes arithmetic / logic commands to output file, given the commands semantics """
        self.output_file.writelines("// " + ' '.join(str(item) for item in semantics[1:]) + "\n")
        
        assembely = self.AL_command_dictionary[semantics[1]] 
        # For commands that need to create unique labels, use i to do so
        if semantics[1] in ["eq", "gt", "lt"]:
            assembely = [sub("i", str(self.i), command) for command in assembely]
            self.i += 1
        
        self.output_file.writelines('\n'.join(assembely) + "\n") # Write the assembely


    def __specialPushPopRegex__(self, semantics, assembely):
        """ Special Command Processing For: static, temp, pointer. Used by the writePushPop() method, implemented for modularity """
        if semantics[2] == "static":
            return([sub("#", str(self.file_name[0:-3]) + str(semantics[3]), command) for command in assembely])
        
        elif semantics[2] == "temp":
            return([sub("#", str(4 + semantics[3]), command) for command in assembely])
        
        elif semantics[2] == "pointer":
            this_that = "THIS" if semantics[3] == 0 else "THAT"
            return([sub("#", this_that, command) for command in assembely])
        
        else: 
            return(assembely) # For non special commands, do nothing


    def writePushPop(self, semantics):
        """ Writes push / pop commands to output file, given the commands semantics """
        self.output_file.writelines("// " + ' '.join(str(item) for item in semantics[1:]) + "\n")
        
        # Assembly generation
        assembely = self.PP_command_dictionary[semantics[2] + " " + semantics[1]]     # Lookup command in the PP comm. dict.
        assembely = [sub("\*", str(semantics[3]), command) for command in assembely]  # Replace placeholder * with the index of the specific command using regex
        assembely = self.__specialPushPopRegex__(semantics, assembely)                # Process special commands
        
        self.output_file.writelines('\n'.join(assembely) + "\n") # Write the assembely


    def writeBranching(self, semantics):
        """ Writes branching commands to output file, given the commands semantics """
        self.output_file.writelines("// " + ' '.join(str(item) for item in semantics[1:]) + "\n")
        
        # Generate assembely
        if semantics[1] == "label":
            assembely = [f'({semantics[2]})']
        elif semantics[1] == "goto":
            assembely = [f"@{semantics[2]}", "0;JMP"]
        elif semantics[1] == "if-goto":
            assembely = ["@SP", "M=M-1", "A=M", "D=M", f"@{semantics[2]}", "D=D+1;JEQ"]
        
        self.output_file.writelines('\n'.join(assembely) + "\n") # Write the assembely


    def close(self):
        self.output_file.close()
