def has_no_e(string):
    if "e" in string:
        return False
    else:
        return True
with open('gadsby_stripped.txt') as f:
    for line in f:
        if has_no_e(line):
            print (line)
            print ("True\n\n\n\n")
        else: print (line + "False\n\n\n\n")
