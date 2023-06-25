# Complete the solution so that it splits the string into pairs of two characters. 
# If the string contains an odd number of characters then it should replace 
# the missing second character of the final pair with an underscore ('_').

# Examples:
# * 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']

def solution(s):
    s_paired = []
    if len(s) % 2 == 0:
        for x in range(len(s) // 2):
            s_paired.append(s[0:2])
            s = s[2:]
    else:
        for x in range(len(s) // 2 + 1):
            s_paired.append(s[0:2])
            s = s[2:]
    if len(s_paired) >= 1:
        if len(s_paired[-1]) == 1:
            s_paired[-1] = s_paired[-1] + '_'
    return s_paired