s = "ahojahojda"

print(s.count('a'))
seznamek = []
for x in s:
    pocet = s.count(x)
    if pocet == 1:
        seznamek.append('(')
    else:
        seznamek.append(")")
print(seznamek)