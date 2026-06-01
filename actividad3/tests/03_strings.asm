.data
_str0: .asciiz "hola mundo"
_str1: .asciiz "RaraLang"
_str2: .asciiz "iteracion 1"

.text
main:
    la $a0, _str0
    li $v0, 4
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    la $a0, _str1
    li $v0, 4
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    la $a0, _str2
    li $v0, 4
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    li $v0, 10
    syscall
