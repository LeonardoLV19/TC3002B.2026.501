.data
_var_add: .word 0
_var_sub: .word 0
_var_div: .word 0

.text
main:
    li $t0, 7
    sw $t0, _var_add
    li $t1, 4
    sw $t1, _var_sub
    li $t2, 2
    sw $t2, _var_div
    lw $t3, _var_add
    move $a0, $t3
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    lw $t4, _var_sub
    move $a0, $t4
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    lw $t5, _var_div
    move $a0, $t5
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    li $v0, 10
    syscall
