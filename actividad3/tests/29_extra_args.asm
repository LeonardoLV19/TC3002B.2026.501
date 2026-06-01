.data
_var_x: .word 0

.text
main:
    li $t0, 5
    li $t1, 99
    move $a0, $t0
    move $a1, $t1
    addiu $sp, $sp, -4
    sw $ra, 0($sp)
    jal doble
    lw $ra, 0($sp)
    addiu $sp, $sp, 4
    move $t2, $v0
    move $a0, $t2
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
