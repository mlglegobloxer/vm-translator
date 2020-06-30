# This program implements a code generator class for the vm translator
# Author: George Duke, Course: Nand to Tetris (ii)

# Import regex character substitution ( the sub() method ) from re
from re import sub

class Generator:
    # Constructor method: create output file, initialise object
    def __init__(self, file_name):
        # Change the file names' extention from .vm to .asm
        self.file_name = file_name[0:-3] + ".asm"
        # Open the output file
        self.output_file = open(self.file_name, "w")

        # Define the AL command dictionary (for arithmetic/logic commands)
        self.AL_command_dictionary = {
            "add": ["@SP", "M=M-1", "A=M", "D=M", "A=A-1", "M=M+D"],
            "sub": ["@SP", "M=M-1", "A=M", "D=M", "A=A-1", "M=M-D"],
            "neg": ["@SP", "A=M-1", "M=-M"],
            "eq" : ["@SP", "M=M-1", "A=M", "D=M", "A=A-1", "@TRUEi", "M=M-D;JEQ", "M=0", "@ENDi", "0;JMP", "(TRUEi)", "D=0", "M=!D", "(ENDi)"],
            "gt" : ["@SP", "M=M-1", "A=M", "D=M", "A=A-1", "@TRUEi", "M=M-D;JGT", "M=0", "@ENDi", "0;JMP", "(TRUEi)", "D=0", "M=!D", "(ENDi)"],
            "lt" : ["@SP", "M=M-1", "A=M", "D=M", "A=A-1", "@TRUEi", "M=M-D;JLT", "M=0", "@ENDi", "0;JMP", "(TRUEi)", "D=0", "M=!D", "(ENDi)"],
            "and": ["@SP", "M=M-1", "A=M", "D=M", "A=A-1", "M=D&M"],
            "or" : ["@SP", "M=M-1", "A=M", "D=M", "A=A-1", "M=D|M"],
            "not": ["@SP", "A=M-1", "M=!M"]
        }

        # Define the PP command dictionary (for push/pop commands)
        self.PP_command_dictionary = {
            "local push"    : ["@LCL", "D=M", "@*", "A=D+A", "D=M", "@SP", "M=M+1", "A=M-1", "M=D"],
            "argument push" : ["@ARG", "D=M", "@*", "A=D+A", "D=M", "@SP", "M=M+1", "A=M-1", "M=D"],
            "this push"     : ["@THIS", "D=M", "@*", "A=D+A", "D=M", "@SP", "M=M+1", "A=M-1", "M=D"],
            "that push"     : ["@THAT", "D=M", "@*", "A=D+A", "D=M", "@SP", "M=M+1", "A=M-1", "M=D"],
            "static push"   : ["@#", "D=M", "@SP", "M=M+1", "A=M-1", "M=D"],
            "pointer push"  : ["@#", "D=A", "@SP", "M=M+1", "A=M-1", "M=D"],
            "temp push"     : ["@#", "D=M", "@SP", "M=M+1", "A=M-1", "M=D"],
            "constant push" : ["@*", "D=A", "@SP", "M=M+1", "A=M-1", "M=D"],
            "local pop"     : ["@LCL", "D=M", "@*", "D=D+A", "@R13", "M=D", "@SP", "M=M-1", "A=M", "D=M", "@R13", "A=M", "M=D"],
            "argument pop"  : ["@ARG", "D=M", "@*", "D=D+A", "@R13", "M=D", "@SP", "M=M-1", "A=M", "D=M", "@R13", "A=M", "M=D"],
            "this pop"      : ["@THIS", "D=M", "@*", "D=D+A", "@R13", "M=D", "@SP", "M=M-1", "A=M", "D=M", "@R13", "A=M", "M=D"],
            "that pop"      : ["@THAT", "D=M", "@*", "D=D+A", "@R13", "M=D", "@SP", "M=M-1", "A=M", "D=M", "@R13", "A=M", "M=D"],
            "static pop"    : ["@SP", "M=M-1", "A=M", "D=M", "@#", "M=D"],
            "pointer pop"   : ["@SP", "M=M-1", "A=M", "D=M", "@#", "M=D"],
            "temp pop"      : ["@SP", "M=M-1", "A=M", "D=M", "@#", "M=D"]
        } 


    def writeArithmetic(self, semantics):
        # Writes arithmetic / logic commands to output file, given the commands semantics #

        # Write the original command commented out
        self.output_file.writelines("// " + ' '.join(str(item) for item in semantics[1:]) + "\n")

        # Generate the assembely by looking up the command in the command dictionary
        assembely = self.AL_command_dictionary[semantics[1]]

        # For commands that need to create unique labels
        if semantics[1] in ["eq", "gt", "lt"]:
            # Replace all references to "i" with the varible i, then increment i
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
        
        # For commmands using pointer replace # with THIS(index = 0) or THAT(index = 1)
        elif semantics[2] == "pointer":
            if semantics[3] == 0:
                this_that = "THIS"
            else:
                this_that = "THAT"

            return([sub("#", this_that, command) for command in assembely])

        else:
            # Command not static, temp, pointer? Do nothing
            return(assembely)


    def writePushPop(self, semantics):
        # Writes push / pop commands to output file, given the commands semantics #

        # Write the original command as a comment (For debugging purposes)
        self.output_file.writelines("// " + ' '.join(str(item) for item in semantics[1:]) + "\n")
        

        # Generate the assembely by looking up the command in the command dictionary
        assembely = self.PP_command_dictionary[semantics[2] + " " + semantics[1]]

        # Replace placeholder * with the index of the specific command using regex
        assembely = [sub("\*", str(semantics[3]), command) for command in assembely]

        ### Command Processing For: static, temp, pointer ###
        assembely = self.__specialPushPopRegex__(semantics, assembely)


        # Write the assembely to the output file
        self.output_file.writelines('\n'.join(assembely) + "\n")


    def close(self):
        # Closes the output file #
        self.output_file.close()