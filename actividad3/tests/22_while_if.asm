.data
_var_x: .word 0

.text
main:
    li $t0, 1
    sw $t0, _var_x
_while_start_0:
    lw $t0, _var_x
    li $t1, 4
    slt $t0, $t0, $t1
    beq $t0, $zero, _while_end_0
    lw $t0, _var_x
    li $t1, 2
    seq $t0, $t0, $t1
    beq $t0, $zero, _if_end_1
    lw $t0, _var_x
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
_if_end_1:
    lw $t0, _var_x
    li $t1, 1
    add $t0, $t0, $t1
    sw $t0, _var_x
    j _while_start_0
_while_end_0:
    li $v0, 10
    syscall
