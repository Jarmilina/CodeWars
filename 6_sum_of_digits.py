# Digital root is the recursive sum of all the digits in a number.
# Given n, take the sum of the digits of n. If that value has more than one digit, 
# continue reducing in this way until a single-digit number is produced. 
# The input will be a non-negative integer.


def digital_root(n):
    if len(str(n)) == 1:
        return n
    else:
        n_digits_summed = 0
        n = str(n)
        for x in n:
            n_digits_summed += int(x)
        return digital_root(n_digits_summed)