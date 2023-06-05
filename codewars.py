def disemvowel(string_):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    string_list = list(string_)
    print(string_list)
    for x in vowels:
            string_list.remove(x) for x in vowels
    print(''.join(string_list))

l = "hello, baby"

disemvowel(l)