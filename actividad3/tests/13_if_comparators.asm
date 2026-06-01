.text
main:
    li $t0, 10
    li $t1, 5
    slt $t0, $t1, $t0
    beq $t0, $zero, _if_end_0
    li $t0, 1
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
_if_end_0:
    li $t0, 3
    li $t1, 7
    slt $t0, $t0, $t1
    beq $t0, $zero, _if_end_1
    li $t0, 1
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
_if_end_1:
    li $t0, 5
    li $t1, 5
    seq $t0, $t0, $t1
    beq $t0, $zero, _if_end_2
    li $t0, 1
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
_if_end_2:
    li $t0, 3
    li $t1, 7
    sne $t0, $t0, $t1
    beq $t0, $zero, _if_end_3
    li $t0, 1
    move $a0, $t0
    li $v0, 1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
_if_end_3:
    li $v0, 10
    syscall
