# The goal of this exercise is to convert a string to a new string where each character
# in the new string is "(" if that character appears only once in the original string,
# or ")" if that character appears more than once in the original string.
# Ignore capitalization when determining if a character is a duplicate.

# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))((" 
# Notes
# Assertion messages may be unclear about what they display in some languages. 
# If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!

def duplicate_encode(word):
    word_l = list(word)
    pass


code = 'hello'
code_l = list(code)

encoded = []

for x in code_l:
    l_list = []
    while x in code_l:
        l_list.append(x)
        code_l.remove(x)
        print(code_l)
        print(l_list)
        if len(l_list) == 1:
            [encoded.append('(') for x in code_l]
            # l_list.append(l)
        if len(l_list) > 1:
            [encoded.append(')') for x in code_l]
            # l_list.append(l)
print(encoded)