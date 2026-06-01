.data
_var_a: .word 0

.text
main:
    li $t0, 5
    sw $t0, _var_a
    lw $t1, _var_a
    move $a0, $t1
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    li $t2, 20
    sw $t2, _var_a
    lw $t3, _var_a
    move $a0, $t3
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    li $v0, 10
    syscall
