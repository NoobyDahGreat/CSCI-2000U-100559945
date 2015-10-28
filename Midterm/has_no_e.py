def has_no_e(word):
    for i in word:
        if i == 'e':
            return False
    else:
        return True

    reader = open('gadsby_stripped.txt', 'r')
    data = reader.readline()
    while line != '':
        if has_no_e(data):
            return True
        else:
            return False
