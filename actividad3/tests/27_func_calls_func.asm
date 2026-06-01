.data
_var_a: .word 0
_var_b: .word 0
_var_x: .word 0

.text
main:
    li $t0, 5
    move $a0, $t0
    addiu $sp, $sp, -4
    sw $ra, 0($sp)
    jal doble
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

suma:
    sw $a0, _var_a
    sw $a1, _var_b
    lw $t0, _var_a
    lw $t1, _var_b
    add $t0, $t0, $t1
    move $v0, $t0
    jr $ra
    jr $ra

doble:
    sw $a0, _var_x
    lw $t0, _var_x
    lw $t1, _var_x
    move $a0, $t0
    move $a1, $t1
    addiu $sp, $sp, -4
    sw $ra, 0($sp)
    jal suma
    lw $ra, 0($sp)
    addiu $sp, $sp, 4
    move $t2, $v0
    move $v0, $t2
    jr $ra
    jr $ra
