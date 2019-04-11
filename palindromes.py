#!python

import string
import re
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)
    # return is_palindrome_lazy(text)

def is_palindrome_lazy(string):
    word = normalize_string(string)
    reverse = word[::-1]
    if reverse == word:
        return True
    else:
        return False

def normalize_string(string):
    """Removes non-letter characters and sets everything to lowercase"""
    new = []
    for char in string: 
        print(char)
        if char.isalpha():
            new.append(char.lower())
    return ''.join(new)
            

def is_palindrome_iterative(text):
    """goes through char by char and returns true if text is a palindrome"""
    for pos in range(len(text)//2):
        print(text[pos])
        if text[pos] != text[-pos]:
            return False
    return True


def is_palindrome_recursive(text, left=None, right=None):
    
    if left is None or right is None:
        left = 0
        right = len(text)-1

    if left >= right:
        return True
    
    print(left, right)
    if text[left].isalpha() and text[right].isalpha():
        if text[left].lower() != text[right].lower():
            return False
        else:
            left += 1
            right -= 1
            return is_palindrome_recursive(text, left, right)
    else:
        if not text[left].isalpha():
            left += 1
        if not text[right].isalpha():
            right -= 1
        return is_palindrome_recursive(text, left, right)

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()