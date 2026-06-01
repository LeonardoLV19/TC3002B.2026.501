.text
main:
    li $t0, 5
    sub $t0, $zero, $t0
    sub $t0, $zero, $t0
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    li $t0, 2
    li $t1, 3
    sll $t0, $t0, 1
    add $t0, $t0, $t1
    li $t2, 1
    add $t0, $t0, $t2
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    li $v0, 10
    syscall
