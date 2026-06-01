.data
_var_x: .word 0
_var_y: .word 0

.text
main:
    li $t0, 10
    sw $t0, _var_x
    li $t1, 3
    sw $t1, _var_y
    lw $t2, _var_x
    move $a0, $t2
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    lw $t3, _var_y
    move $a0, $t3
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    li $v0, 10
    syscall
