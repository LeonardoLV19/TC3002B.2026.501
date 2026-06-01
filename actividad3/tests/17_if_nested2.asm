.data
_var_x: .word 0

.text
main:
    li $t0, 7
    sw $t0, _var_x
    lw $t0, _var_x
    li $t1, 5
    slt $t0, $t1, $t0
    beq $t0, $zero, _if_else_0
    lw $t0, _var_x
    li $t1, 10
    slt $t0, $t1, $t0
    beq $t0, $zero, _if_else_1
    li $t0, 99
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    j _if_end_1
_if_else_1:
    li $t0, 7
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
_if_end_1:
    j _if_end_0
_if_else_0:
    li $t0, 0
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
_if_end_0:
    li $v0, 10
    syscall
