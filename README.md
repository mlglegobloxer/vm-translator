# VM Translator
My implementation of the vm-translator from the NAND to Tetris course on corsera


This program maps hack vm code:

    // Calculates (local 1) modulo 7 (inefficently)

    push constant 0
    pop  temp     1

    label WHILE_INCOMPLETE
        push local 1
        push constant 7
        sub

        lt
        if-goto END

        pop  local 1
        goto WHILE_INCOMPLETE

    label END

To hack assembely:

    ...
    // label WHILE_INCOMPLETE
    (WHILE_INCOMPLETE)
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
    // push constant 7
    @7
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
    ...
