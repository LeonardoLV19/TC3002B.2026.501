.data
_var_x: .word 0
_var_y: .word 0

.text
main:
    li $t0, 10
    sw $t0, _var_x
    li $t0, 3
    sw $t0, _var_y
    lw $t0, _var_x
    lw $t1, _var_y
    add $t0, $t0, $t1
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    lw $t0, _var_x
    lw $t1, _var_y
    sub $t0, $t0, $t1
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    lw $t0, _var_x
    lw $t1, _var_y
    mult $t0, $t1
    mflo $t0
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    lw $t0, _var_x
    lw $t1, _var_y
    div $t0, $t1
    mflo $t0
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    lw $t0, _var_x
    li $t1, 2
    add $t0, $t0, $t1
    lw $t2, _var_y
    li $t3, 1
    sub $t2, $t2, $t3
    mult $t0, $t2
    mflo $t0
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    li $v0, 10
    syscall
