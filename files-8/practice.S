.eqv BUFFER_SIZE 10
.eqv STDIN 0
.eqv STDOUT 1
.eqv NL 10
.eqv SIMPLE_READ 8
.eqv SIMPLE_WRITE 4

.data
mybuffer: .space BUFFER_SIZE
str_char: .string "Char value read !"
str_int: .string "Int value read !"
str_str: .string "String read !"
newline: .string "\n"
excl: .string "!"

.text
.globl main
main:
    # Read a character
    li a7, 12  # ecall code for read character
    ecall
    mv s1, a0  # Store character in s1

    # Read an integer
    li a7, 5  # ecall code for read integer
    ecall
    mv s2, a0  # Store integer in s2

read_string:
    # Read a string
    li a7, SIMPLE_READ
    la a0, mybuffer
    li a1, BUFFER_SIZE
    ecall
    mv s3, a0  # Store number of chars read

    # Check for newline (empty input case)
    la t0, mybuffer
    lb t1, 0(t0)  # Load first character
    li t2, NL
    beq t1, t2, eof_reached  # If newline, we reached EOF

    # Print "String read is !"
    li a7, SIMPLE_WRITE
    la a0, str_str
    ecall

    # Print the actual string
    li a7, SIMPLE_WRITE
    la a0, mybuffer
    ecall

    # Print "!"
    li a7, SIMPLE_WRITE
    la a0, excl
    ecall

    # Print newline
    li a7, SIMPLE_WRITE
    la a0, newline
    ecall

    j read_string  # Read another string

eof_reached:
    # Print "Char value read is !"
    li a7, SIMPLE_WRITE
    la a0, str_char
    ecall

    # Print character value
    mv a0, s1
    li a7, 11  # Print character syscall
    ecall

    # Print "!"
    li a7, SIMPLE_WRITE
    la a0, excl
    ecall

    # Print newline
    li a7, SIMPLE_WRITE
    la a0, newline
    ecall

    # Print "Int value read is !"
    li a7, SIMPLE_WRITE
    la a0, str_int
    ecall

    # Print integer value
    mv a0, s2
    li a7, 1  # Print integer syscall
    ecall

    # Print "!"
    li a7, SIMPLE_WRITE
    la a0, excl
    ecall

    # Print newline
    li a7, SIMPLE_WRITE
    la a0, newline
    ecall

    # Exit program
    li a7, 10
    ecall
