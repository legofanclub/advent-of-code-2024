def solve():
    output = []
    A = 24847151
    B = 0
    C = 0

    # manually describe operations of program
    while A != 0:
        B = A % 8
        B = B ^ 5
        C = A // (2**B) # can modulo this result and get the same answer
        B = B ^ 6
        A = A // (2**3)
        B = B ^ C
        output.append(B % 8)

    return ",".join([str(x) for x in output])

print(solve())
