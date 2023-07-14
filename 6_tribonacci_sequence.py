# As the name may already reveal, it works basically like a Fibonacci, 
# but summing the last 3 (instead of 2) numbers of the sequence to generate the next. 
# So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature), 
# we have this sequence:
# [1, 1 ,1, 3, 5, 9, 17, 31, ...]
# You need to create a fibonacci function that given a signature array/list, 
# returns the first n elements - signature included of the so seeded sequence.
# Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0, 
# then return an empty array (except in C return NULL) 
# and be ready for anything else which is not clearly specified

def tribonacci(signature, n):
    tribonacci_sequence = signature
    if n <= 3:
        return tribonacci_sequence[0:n]
    else:
        for x in range(n-3):
            tribonacci_sequence.append(sum(tribonacci_sequence[x:(x+3)]))
        return tribonacci_sequence