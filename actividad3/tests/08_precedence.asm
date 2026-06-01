.text
main:
    li $t0, 2
    li $t1, 3
    li $t2, 4
    mult $t1, $t2
    mflo $t1
    add $t0, $t0, $t1
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    li $t0, 2
    li $t1, 3
    add $t0, $t0, $t1
    li $t2, 4
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
