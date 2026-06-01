.data
_var_x: .word 0
_var_y: .word 0

.text
main:
    li $t0, 5
    sw $t0, _var_x
    li $t0, 3
    sw $t0, _var_y
    lw $t0, _var_x
    li $t1, 0
    slt $t0, $t1, $t0
    beq $t0, $zero, _if_end_0
    lw $t0, _var_y
    li $t1, 0
    slt $t0, $t1, $t0
    beq $t0, $zero, _if_else_1
    lw $t0, _var_x
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    j _if_end_1
_if_else_1:
    li $t0, 0
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
_if_end_1:
_if_end_0:
    lw $t0, _var_x
    li $t1, 0
    slt $t0, $t1, $t0
    li $t2, 1
    seq $t0, $t0, $t2
    beq $t0, $zero, _if_end_2
    li $t0, 99
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
_if_end_2:
    li $v0, 10
    syscall
