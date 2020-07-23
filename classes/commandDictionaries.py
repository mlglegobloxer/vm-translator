# This program implements a command dictionary containing the generalised assembely for each command
# Author: George Duke, Course: Nand to Tetris (ii)


# Define the AL command dictionary (for arithmetic/logic commands)
AL_command_dictionary = {
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
PP_command_dictionary = {
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