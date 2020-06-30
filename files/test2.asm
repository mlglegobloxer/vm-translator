// set SP = 256
@256
D=A
@SP
M=D
// add
@SP
M=M-1
A=M
D=M
A=A-1
M=M+D
// sub
@SP
M=M-1
A=M
D=M
A=A-1
M=M-D
// neg
@SP
A=M-1
M=-M
// eq
@SP
M=M-1
A=M
D=M
A=A-1
@TRUE0
M=M-D;JEQ
M=0
@END0
0;JMP
(TRUE0)
D=0
M=!D
(END0)
// gt
@SP
M=M-1
A=M
D=M
A=A-1
@TRUE1
M=M-D;JGT
M=0
@END1
0;JMP
(TRUE1)
D=0
M=!D
(END1)
// lt
@SP
M=M-1
A=M
D=M
A=A-1
@TRUE2
M=M-D;JLT
M=0
@END2
0;JMP
(TRUE2)
D=0
M=!D
(END2)
// and
@SP
M=M-1
A=M
D=M
A=A-1
M=D&M
// or
@SP
M=M-1
A=M
D=M
A=A-1
M=D|M
// not
@SP
A=M-1
M=!M
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
@test2.6
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
@test2.7
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
