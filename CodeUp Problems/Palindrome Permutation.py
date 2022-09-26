def Palindrome(char):
    i = 0
    ctr = 0
    char = char.upper()
    org = char.upper()
    char = list(char)
    org = list(org)
    while ctr < 99:
        if i < len(org) - 1:
            char.reverse()
            rev = "".join(char)
            org = "".join(org)
            if rev == org:
                return True
            else:
                char = list(char)
                org = list(org)
                sto = org[i]
                org[i] = org[i + 1]
                org[i + 1] = sto
                i = i + 1
                ctr = ctr + 1
        else:
            char.reverse()
            rev = "".join(char)
            org = "".join(org)
            if rev == org:
                return True
            else:
                i = 0
                char = list(char)
                org = list(org)
                sto = org[i]
                org[i] = org[i - 1]
                org[i - 1] = sto
                i = i + 1
                ctr = ctr + 1
    return False

# test case
#x = Palindrome("taett")
#print(x)