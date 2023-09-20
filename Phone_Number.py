def isPhoneNumber(txt):
    if len(txt) != 13:
        return False
    else:
        if txt[0] != '(':
            return False
        for i in txt[1:4]:
            if not i.isdecimal():
                return False
        if txt[4] != ')':
            return False
        if txt[8] != '-':
            return False
        for i in txt[5:8] + txt[9:]:
            if not i.isdecimal():
                return False
    return True

#test
print(isPhoneNumber("(319)-404-2331"))
