def input_string(message):
    string = f"{input(message)}"
    return string

def input_integer(message):
    integ = int(input(message))
    return integ

def input_real(message):
    real = input(message)*1.00
    return real

def input_boolean(message):
    bol = input(message)
    if bol=="y":
        return True
    elif bol=="n":
        return False
    else:
        return bol