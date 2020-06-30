// push constant 5
@5
D=A
@SP
M=M+1
A=M-1
M=D
// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D
// add
@SP
M=M-1
A=M
D=M
A=A-1
M=M+D
// pop local 1
@LCL
D=M
@1
D=D+A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
// push constant 10
@10
D=A
@SP
M=M+1
A=M-1
M=D
// push local 1
@LCL
D=M
@1
A=D+A
D=M
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
@TRUE0
M=M-D;JLT
M=0
@END0
0;JMP
(TRUE0)
D=0
M=!D
(END0)
// push static 3
@five-plus-three.3
D=M
@SP
M=M+1
A=M-1
M=D
