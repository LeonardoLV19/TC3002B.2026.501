.text
main:
    li $t0, 10
    li $t1, 3
    div $t0, $t1
    mfhi $t0
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    li $t0, 4
    li $t1, 5
    sll $t0, $t0, 1
    add $t0, $t0, $t1
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    li $t0, 7
    li $t1, 3
    add $t0, $t0, $t1
    sra $t0, $t0, 1
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    li $t0, 8
    sub $t0, $zero, $t0
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    li $v0, 10
    syscall
