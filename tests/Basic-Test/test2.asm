// Set SP to 256
@256
D=A
@SP
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
// push argument 2
@ARG
D=M
@2
A=D+A
D=M
@SP
M=M+1
A=M-1
M=D
// push this 3
@THIS
D=M
@3
A=D+A
D=M
@SP
M=M+1
A=M-1
M=D
// push that 4
@THAT
D=M
@4
A=D+A
D=M
@SP
M=M+1
A=M-1
M=D
// push constant 5
@5
D=A
@SP
M=M+1
A=M-1
M=D
// push static 6
@tests/Basic-Test/test2.6
D=M
@SP
M=M+1
A=M-1
M=D
// push pointer 1
@THAT
D=A
@SP
M=M+1
A=M-1
M=D
// push temp 1
@5
D=M
@SP
M=M+1
A=M-1
M=D
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
// pop argument 1
@ARG
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
// pop this 1
@THIS
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
// pop that 1
@THAT
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
// pop static 7
@SP
M=M-1
A=M
D=M
@tests/Basic-Test/test2.7
M=D
// pop pointer 1
@SP
M=M-1
A=M
D=M
@THAT
M=D
// pop temp 1
@SP
M=M-1
A=M
D=M
@5
M=D
