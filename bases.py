#!python3

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace

class Base():
    """power : digit
    Example: base2 (binary)
    {0: 2^0
    1: 2^1}"""
    def __init__(self, base):
        super().__init__()
        # wait do I need this?
        self.base = base
        self.digits = ""
        self.exponents = {}


def decode_unary(num): # for fun
    string = ""
    for _ in range(num):
        string = string + "."
    return string


def decode_digit(char, base):
    '''Returns an int of what number a char represents for the given base'''
    if base == 16:
        # use hexdigits
        return string.hexdigits.index(char)
    elif base >= 10:
        return string.printable.index(char)
    else:
        return int(char)


def encode_digit(digit, base):
    """Takes an int and returns a base representation of it"""
    if base == 16:
        # special treatment for hexdigits
        return string.hexdigits[digit]
    else:
        return string.printable[digit]
        

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    total = 0
    power = 0
    for character in digits[::-1]: # go through them in reverse
        digit = decode_digit(character, base)
        digit_value = digit*(base**power)
        power += 1
        total += digit_value
    return total


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    
    digits = []
    while number > 0:
        remainder = number % base
        number = number // base
        digit = encode_digit(remainder, base)
        digits.append(digit)
    # return the reversed and stringified list
    return "".join(digits[::-1]) 


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    decoded = decode(digits, base1)
    return encode(decoded, base2)


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()