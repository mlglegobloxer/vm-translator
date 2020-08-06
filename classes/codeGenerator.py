# This program implements a code generator class for the vm translator
# Author: George Duke, Course: Nand to Tetris (ii)

# Import regex character substitution and the command dictionaries
from re import sub
from classes.commandDictionaries import *

class Generator:
    def __init__(self, file_name):
        self.file_name = file_name
        self.output_file = open(self.file_name, "w")

        # Define the command dictonaries for all command types
        self.AL_command_dictionary = AL_command_dictionary
        self.PP_command_dictionary = PP_command_dictionary
        self.Return_command_list = Return_command_list
        self.Call_command_list = Call_command_list
        
        # Define a varible used to generate unique labels for commands that require them 
        self.i = 1

        # Set the initial state of the stack machine
        self.output_file.writelines('\n'.join(Init_command_list) + "\n")
        
        
    def writeArithmetic(self, semantics):
        """ Writes arithmetic / logic commands to output file, given the commands semantics """
        self.writeComment(semantics)
        
        assembely = self.AL_command_dictionary[semantics[1]] 
        # For commands that need to create unique labels, use i to do so
        if semantics[1] in ["eq", "gt", "lt"]:
            assembely = [sub("i", str(self.i), command) for command in assembely]
            self.i += 1
        
        self.writeAssembely(assembely)


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
        self.writeComment(semantics)
        
        # Assembly generation
        assembely = self.PP_command_dictionary[semantics[2] + " " + semantics[1]]     # Lookup command in the PP comm. dict.
        assembely = [sub("\*", str(semantics[3]), command) for command in assembely]  # Replace placeholder * with the index of the specific command using regex
        assembely = self.__specialPushPopRegex__(semantics, assembely)                # Process special commands

        self.writeAssembely(assembely)


    def writeBranching(self, semantics):
        """ Writes branching commands to output file, given the commands semantics """
        self.writeComment(semantics)
        
        # Generate assembely
        if semantics[1] == "label":
            assembely = [f'({semantics[2]})']
        elif semantics[1] == "goto":
            assembely = [f"@{semantics[2]}", "0;JMP"]
        elif semantics[1] == "if-goto":
            assembely = ["@SP", "M=M-1", "A=M", "D=M", f"@{semantics[2]}", "D=D+1;JEQ"]
        
        self.writeAssembely(assembely)


    def writeFunction(self, semantics):
        """ Writes function declarations to output file, given semantics """
        self.writeComment(semantics)

        assembely = [f"({str(semantics[2])})"] + (["@SP", "M=M+1", "A=M-1", "M=0"] * semantics[3])

        self.writeAssembely(assembely)


    def writeCall(self, semantics):
        """ Writes function calls to output file, given semantics """
        self.writeComment(semantics)

        # Assembely generation
        assembely = self.Call_command_list
        assembely = [sub("functionName", semantics[2], command) for command in assembely]
        assembely = [sub("decrement_val", str(5 + semantics[3]), command) for command in assembely]
        assembely = [sub("#", str(self.i), command) for command in assembely]
        
        self.i += 1 # Increment i
        
        self.writeAssembely(assembely)


    def writeReturn(self, semantics):
        """ Writes function return commands to output file, given semantics """
        self.writeComment(semantics)

        assembely = self.Return_command_list

        self.writeAssembely(assembely)


    def writeComment(self, semantics):
        self.output_file.writelines("// " + ' '.join(str(item) for item in semantics[1:]) + "\n")


    def writeAssembely(self, assembely):
        self.output_file.writelines('\n'.join(assembely) + "\n")


    def close(self):
        self.output_file.close()
