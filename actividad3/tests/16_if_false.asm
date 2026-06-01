.data
_var_x: .word 0

.text
main:
    li $t0, 3
    sw $t0, _var_x
    lw $t0, _var_x
    li $t1, 10
    slt $t0, $t1, $t0
    beq $t0, $zero, _if_end_0
    li $t0, 1
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
_if_end_0:
    li $v0, 10
    syscall
