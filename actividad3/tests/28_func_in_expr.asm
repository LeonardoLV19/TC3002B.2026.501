.data
_var_x: .word 0

.text
main:
    li $t0, 3
    move $a0, $t0
    addiu $sp, $sp, -4
    sw $ra, 0($sp)
    jal doble
    lw $ra, 0($sp)
    addiu $sp, $sp, 4
    move $t1, $v0
    li $t2, 1
    add $t1, $t1, $t2
    move $a0, $t1
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    li $v0, 10
    syscall

doble:
    sw $a0, _var_x
    lw $t0, _var_x
    lw $t1, _var_x
    add $t0, $t0, $t1
    move $v0, $t0
    jr $ra
    jr $ra
