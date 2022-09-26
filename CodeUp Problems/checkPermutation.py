def checkPermutation(str1, str2):
    str1 = str(str1)
    str2 = str(str2)
    if str1 == str2:
        return False
    elif len(str1) != len(str2):
        return False
    for i in str1:
        if i not in str2:
            return False
    for i in str2:
        if i not in str1:
            return False
    return True

# test cases
checkPermutation('cat', 'tca')
checkPermutation('dog', 'dog')
checkPermutation('dog', 'cat')
checkPermutation('cat', 'dogs')
checkPermutation('$^&$', 2343)
checkPermutation(1234, 4321)