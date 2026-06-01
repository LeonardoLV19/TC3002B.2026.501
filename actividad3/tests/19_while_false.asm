.data
_var_x: .word 0

.text
main:
    li $t0, 10
    sw $t0, _var_x
_while_start_0:
    lw $t0, _var_x
    li $t1, 5
    slt $t0, $t0, $t1
    beq $t0, $zero, _while_end_0
    lw $t0, _var_x
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    j _while_start_0
_while_end_0:
    li $v0, 10
    syscall
