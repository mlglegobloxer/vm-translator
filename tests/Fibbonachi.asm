// Set SP to 256
@256
D=A
@SP
M=D
// call Sys.init 0
@Sys.init$ret.0
D=A
@SP
M=M+1
A=M-1
M=D
@LCL
D=M
@SP
M=M+1
A=M-1
M=D
@ARG
D=M
@SP
M=M+1
A=M-1
M=D
@THIS
D=M
@SP
M=M+1
A=M-1
M=D
@THAT
D=M
@SP
M=M+1
A=M-1
M=D
@SP
D=M
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.init
0;JMP
(Sys.init$ret.0)
// function Main.fibonacci 0
(Main.fibonacci)
// push argument 0
@ARG
D=M
@0
A=D+A
D=M
@SP
M=M+1
A=M-1
M=D
// push constant 2
@2
D=A
@SP
M=M+1
A=M-1
M=D
// lt
@SP
M=M-1
A=M
D=M
A=A-1
@TRUE1
M=M-D;JLT
M=0
@END1
0;JMP
(TRUE1)
D=0
M=!D
(END1)
// if-goto IF_TRUE
@SP
M=M-1
A=M
D=M
@IF_TRUE
D=D+1;JEQ
// goto IF_FALSE
@IF_FALSE
0;JMP
// label IF_TRUE
(IF_TRUE)
// push argument 0
@ARG
D=M
@0
A=D+A
D=M
@SP
M=M+1
A=M-1
M=D
// return
@LCL
D=M
@R14
M=D
@5
D=D-A
A=D
D=M
@R15
M=D
@SP
M=M-1
A=M
D=M
@R13
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@R14
M=M-1
A=M
D=M
@THAT
M=D
@R14
M=M-1
A=M
D=M
@THIS
M=D
@R14
M=M-1
A=M
D=M
@ARG
M=D
@R14
M=M-1
A=M
D=M
@LCL
M=D
@R15
A=M
0;JMP
// label IF_FALSE
(IF_FALSE)
// push argument 0
@ARG
D=M
@0
A=D+A
D=M
@SP
M=M+1
A=M-1
M=D
// push constant 2
@2
D=A
@SP
M=M+1
A=M-1
M=D
// sub
@SP
M=M-1
A=M
D=M
A=A-1
M=M-D
// call Main.fibonacci 1
@Main.fibonacci$ret.2
D=A
@SP
M=M+1
A=M-1
M=D
@LCL
D=M
@SP
M=M+1
A=M-1
M=D
@ARG
D=M
@SP
M=M+1
A=M-1
M=D
@THIS
D=M
@SP
M=M+1
A=M-1
M=D
@THAT
D=M
@SP
M=M+1
A=M-1
M=D
@SP
D=M
@6
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.2)
// push argument 0
@ARG
D=M
@0
A=D+A
D=M
@SP
M=M+1
A=M-1
M=D
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// sub
@SP
M=M-1
A=M
D=M
A=A-1
M=M-D
// call Main.fibonacci 1
@Main.fibonacci$ret.3
D=A
@SP
M=M+1
A=M-1
M=D
@LCL
D=M
@SP
M=M+1
A=M-1
M=D
@ARG
D=M
@SP
M=M+1
A=M-1
M=D
@THIS
D=M
@SP
M=M+1
A=M-1
M=D
@THAT
D=M
@SP
M=M+1
A=M-1
M=D
@SP
D=M
@6
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.3)
// add
@SP
M=M-1
A=M
D=M
A=A-1
M=M+D
// return
@LCL
D=M
@R14
M=D
@5
D=D-A
A=D
D=M
@R15
M=D
@SP
M=M-1
A=M
D=M
@R13
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@R14
M=M-1
A=M
D=M
@THAT
M=D
@R14
M=M-1
A=M
D=M
@THIS
M=D
@R14
M=M-1
A=M
D=M
@ARG
M=D
@R14
M=M-1
A=M
D=M
@LCL
M=D
@R15
A=M
0;JMP
// function Sys.init 0
(Sys.init)
// push constant 4
@4
D=A
@SP
M=M+1
A=M-1
M=D
// call Main.fibonacci 1
@Main.fibonacci$ret.4
D=A
@SP
M=M+1
A=M-1
M=D
@LCL
D=M
@SP
M=M+1
A=M-1
M=D
@ARG
D=M
@SP
M=M+1
A=M-1
M=D
@THIS
D=M
@SP
M=M+1
A=M-1
M=D
@THAT
D=M
@SP
M=M+1
A=M-1
M=D
@SP
D=M
@6
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.4)
// label WHILE
(WHILE)
// goto WHILE
@WHILE
0;JMP
