def encrypt(text,rot):
    secret=""
    for let in text:
        secret=secret+rotate_character(let,rot)
    return secret


def alphabet_position(letter):
    alphabet="aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
    pos=alphabet.index(letter)//2
    return pos


def rotate_character(char,rot):
    alphabet="aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
    rotI=0
    if char not in alphabet:
        charNew=char
    else:
        rotI=alphabet.index(char)+int(rot)*2
        if rotI<52:
            charNew=alphabet[rotI]
        else:
            charNew=alphabet[rotI%52]
        if alphabet.index(char)%2 != 0:
            return charNew.upper()
    return charNew
