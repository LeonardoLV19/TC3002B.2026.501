.data
_var_a: .word 0
_var_b: .word 0
_var_c: .word 0

.text
main:
    li $t0, 3
    sub $t0, $zero, $t0
    sw $t0, _var_a
    li $t0, 1
    sub $t0, $zero, $t0
    sw $t0, _var_b
    li $t0, 2
    sub $t0, $zero, $t0
    sw $t0, _var_c
    lw $t0, _var_a
    lw $t1, _var_b
    add $t0, $t0, $t1
    sra $t0, $t0, 1
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    lw $t0, _var_a
    lw $t1, _var_c
    add $t0, $t0, $t1
    sra $t0, $t0, 1
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    li $v0, 10
    syscall
