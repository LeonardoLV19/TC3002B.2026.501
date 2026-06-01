.data
_var_i: .word 0
_var_j: .word 0
_var_k: .word 0

.text
main:
    li $t0, 1
    sw $t0, _var_i
_while_start_0:
    lw $t0, _var_i
    li $t1, 3
    slt $t0, $t0, $t1
    beq $t0, $zero, _while_end_0
    li $t0, 1
    sw $t0, _var_j
_while_start_1:
    lw $t0, _var_j
    li $t1, 3
    slt $t0, $t0, $t1
    beq $t0, $zero, _while_end_1
    li $t0, 1
    sw $t0, _var_k
_while_start_2:
    lw $t0, _var_k
    li $t1, 3
    slt $t0, $t0, $t1
    beq $t0, $zero, _while_end_2
    lw $t0, _var_k
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    lw $t0, _var_k
    li $t1, 1
    add $t0, $t0, $t1
    sw $t0, _var_k
    j _while_start_2
_while_end_2:
    lw $t0, _var_j
    li $t1, 1
    add $t0, $t0, $t1
    sw $t0, _var_j
    j _while_start_1
_while_end_1:
    lw $t0, _var_i
    li $t1, 1
    add $t0, $t0, $t1
    sw $t0, _var_i
    j _while_start_0
_while_end_0:
    li $v0, 10
    syscall
