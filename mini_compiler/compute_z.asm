.section .data
    a: .long 8
    b: .long 4
    z: .long 0
    newline: .asciz "\n"

    .section .bss
    buffer: .space 12

    .section .text
    .global _start
    _start:
        mov a(%rip), %eax
        imul %eax, %eax
        mov %eax, %r8d

        mov b(%rip), %eax
        imul %eax, %eax
        add %eax, %r8d

        mov a(%rip), %eax
        imul b(%rip), %eax
        add %eax, %eax
        sub %eax, %r8d

        mov %r8d, z(%rip)

        # Convert integer to string
        lea buffer(%rip), %rsi
        mov %r8d, %edi
        call int_to_str

        # Print buffer
        mov $1, %rax
        mov $1, %rdi
        lea buffer(%rip), %rsi
        mov $12, %rdx
        syscall

        # Print newline
        mov $1, %rax
        mov $1, %rdi
        lea newline(%rip), %rsi
        mov $1, %rdx
        syscall

        # Exit
        mov $60, %rax
        xor %rdi, %rdi
        syscall

    int_to_str:
        mov %rsi, %rcx
        add $11, %rcx
        movb $0, (%rcx)
        dec %rcx

        mov %edi, %eax
        cmp $0, %eax
        jge .convert

        neg %eax
        movb $'-', (%rsi)
        inc %rsi

    .convert:
        xor %edx, %edx
        mov $10, %ebx

    .loop:
        xor %edx, %edx
        div %ebx
        add $'0', %edx
        mov %dl, (%rcx)
        dec %rcx
        test %eax, %eax
        jnz .loop

        inc %rcx
        mov %rcx, %rsi
        ret
