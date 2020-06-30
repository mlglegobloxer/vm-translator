@256
D=A
@SP
M=D// push constant 111
@111
D=A
@SP
M=M+1
A=M-1
M=D
// push constant 333
@333
D=A
@SP
M=M+1
A=M-1
M=D
// push constant 888
@888
D=A
@SP
M=M+1
A=M-1
M=D
// pop static 8
@SP
M=M-1
A=M
D=M
@files/StaticTest.8
M=D
// pop static 3
@SP
M=M-1
A=M
D=M
@files/StaticTest.3
M=D
// pop static 1
@SP
M=M-1
A=M
D=M
@files/StaticTest.1
M=D
// push static 3
@files/StaticTest.3
D=M
@SP
M=M+1
A=M-1
M=D
// push static 1
@files/StaticTest.1
D=M
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
// push static 8
@files/StaticTest.8
D=M
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
