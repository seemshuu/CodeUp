def isUnique(input_str):
    for i in input_str:
        if input_str.count(i) != 1:
            return False
    return True

# test cases
#isUnique('qwertyuiio')
#isUnique('aswerot ivnx23')
#isUnique('12345asdf@^^')
#isUnique('5234perdant|}{|@')
#isUnique("TUP<3")
