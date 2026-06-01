.data
_var_x: .word 0

.text
main:
    li $t0, 1
    move $a0, $t0
    addiu $sp, $sp, -4
    sw $ra, 0($sp)
    jal cuenta
    lw $ra, 0($sp)
    addiu $sp, $sp, 4
    move $t1, $v0
    move $a0, $t1
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    li $v0, 10
    syscall

cuenta:
    sw $a0, _var_x
    lw $t0, _var_x
    li $t1, 1
    add $t0, $t0, $t1
    move $a0, $t0
    addiu $sp, $sp, -4
    sw $ra, 0($sp)
    jal cuenta
    lw $ra, 0($sp)
    addiu $sp, $sp, 4
    move $t2, $v0
    move $v0, $t2
    jr $ra
    jr $ra
