# This program implements a command dictionary containing the generalised assembely for each command 
# Author: George Duke, Course: Nand to Tetris (ii)

# Define a list of commands to set the inital state of the command dictionary
Init_command_list = ["// Set SP to 256", "@256", "D=A", "@SP", "M=D",
                     "// call Sys.init 0",
                     "@Sys.init$ret.0", "D=A", "@SP", "M=M+1", "A=M-1", "M=D",
                     "@LCL", "D=M", "@SP", "M=M+1", "A=M-1", "M=D",
                     "@ARG", "D=M", "@SP", "M=M+1", "A=M-1", "M=D",
                     "@THIS", "D=M", "@SP", "M=M+1", "A=M-1", "M=D",
                     "@THAT", "D=M", "@SP", "M=M+1", "A=M-1", "M=D",
                     "@SP", "D=M", "@5", "D=D-A", "@ARG", "M=D",
                     "@SP", "D=M", "@LCL", "M=D",
                     "@Sys.init", "0;JMP", "(Sys.init$ret.0)"
]

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


# Define the list of commands to be written at call
Call_command_list = [
    "@functionName$ret.#", "D=A", "@SP", "M=M+1", "A=M-1", "M=D",
    "@LCL", "D=M", "@SP", "M=M+1", "A=M-1", "M=D",
    "@ARG", "D=M", "@SP", "M=M+1", "A=M-1", "M=D",
    "@THIS", "D=M", "@SP", "M=M+1", "A=M-1", "M=D",
    "@THAT", "D=M", "@SP", "M=M+1", "A=M-1", "M=D",
    "@SP", "D=M", "@decrement_val", "D=D-A", "@ARG", "M=D",
    "@SP", "D=M", "@LCL", "M=D",
    "@functionName", "0;JMP", "(functionName$ret.#)"
]


Return_command_list = [
    "@LCL", "D=M", "@R14", "M=D",
    "@5", "D=D-A", "A=D", "D=M", "@R15", "M=D",
    "@SP", "M=M-1", "A=M", "D=M", "@R13", "@ARG", "A=M", "M=D",
    "@ARG", "D=M+1", "@SP", "M=D",
    "@R14", "M=M-1", "A=M", "D=M", "@THAT", "M=D",
    "@R14", "M=M-1", "A=M", "D=M", "@THIS", "M=D",
    "@R14", "M=M-1", "A=M", "D=M", "@ARG", "M=D",
    "@R14", "M=M-1", "A=M", "D=M", "@LCL", "M=D",
    "@R15", "A=M", "0;JMP"
]
