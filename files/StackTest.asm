// set SP = 256
@256
D=A
@SP
M=D
// push constant 17
@17
D=A
@SP
M=M+1
A=M-1
M=D
// push constant 17
@17
D=A
@SP
M=M+1
A=M-1
M=D
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
// push constant 17
@17
D=A
@SP
M=M+1
A=M-1
M=D
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// eq
@SP
M=M-1
A=M
D=M
A=A-1
@TRUE1
M=M-D;JEQ
M=0
@END1
0;JMP
(TRUE1)
D=0
M=!D
(END1)
// push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
// push constant 17
@17
D=A
@SP
M=M+1
A=M-1
M=D
// eq
@SP
M=M-1
A=M
D=M
A=A-1
@TRUE2
M=M-D;JEQ
M=0
@END2
0;JMP
(TRUE2)
D=0
M=!D
(END2)
// push constant 892
@892
D=A
@SP
M=M+1
A=M-1
M=D
// push constant 891
@891
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
@TRUE3
M=M-D;JLT
M=0
@END3
0;JMP
(TRUE3)
D=0
M=!D
(END3)
// push constant 891
@891
D=A
@SP
M=M+1
A=M-1
M=D
// push constant 892
@892
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
@TRUE4
M=M-D;JLT
M=0
@END4
0;JMP
(TRUE4)
D=0
M=!D
(END4)
// push constant 891
@891
D=A
@SP
M=M+1
A=M-1
M=D
// push constant 891
@891
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
@TRUE5
M=M-D;JLT
M=0
@END5
0;JMP
(TRUE5)
D=0
M=!D
(END5)
// push constant 32767
@32767
D=A
@SP
M=M+1
A=M-1
M=D
// push constant 32766
@32766
D=A
@SP
M=M+1
A=M-1
M=D
// gt
@SP
M=M-1
A=M
D=M
A=A-1
@TRUE6
M=M-D;JGT
M=0
@END6
0;JMP
(TRUE6)
D=0
M=!D
(END6)
// push constant 32766
@32766
D=A
@SP
M=M+1
A=M-1
M=D
// push constant 32767
@32767
D=A
@SP
M=M+1
A=M-1
M=D
// gt
@SP
M=M-1
A=M
D=M
A=A-1
@TRUE7
M=M-D;JGT
M=0
@END7
0;JMP
(TRUE7)
D=0
M=!D
(END7)
// push constant 32766
@32766
D=A
@SP
M=M+1
A=M-1
M=D
// push constant 32766
@32766
D=A
@SP
M=M+1
A=M-1
M=D
// gt
@SP
M=M-1
A=M
D=M
A=A-1
@TRUE8
M=M-D;JGT
M=0
@END8
0;JMP
(TRUE8)
D=0
M=!D
(END8)
// push constant 57
@57
D=A
@SP
M=M+1
A=M-1
M=D
// push constant 31
@31
D=A
@SP
M=M+1
A=M-1
M=D
// push constant 53
@53
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
// push constant 112
@112
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
// neg
@SP
A=M-1
M=-M
// and
@SP
M=M-1
A=M
D=M
A=A-1
M=D&M
// push constant 82
@82
D=A
@SP
M=M+1
A=M-1
M=D
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
