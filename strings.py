#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)

    return find_index(text, pattern) is not None


def find_index(text, pattern, start_index=-1):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found.
    Time complexity is length of text * lenght of the pattern (worst case) evens out to O(n) where n is text length in the average case
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    

    start_index += 1 # this is iffy

    # ok so now we need to iterate through the text STARTING at the start index
    for index in range(start_index, len(text)):
        # is char (index, char) pattern[0]? also start at a certain point
        if pattern == "":
            return start_index

        if text[index] in pattern[0]:
            match_index = index # we match this against the corresponding char in the pattern
            for pattern_char in pattern:
                try:
                    if pattern_char in text[match_index]:
                        match_index += 1
                    else:
                        break # one of these didn't match
                        # wait will this just break out of the for loop?
                except IndexError:
                    return None
            else:
                return index # this should work??


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)
    return list(generate_all_indexes(text, pattern))


def generate_all_indexes(text, pattern):
    """
    Also O(n) for the same reasons
    """
    patterns = []
    last_index = -1
    for index in range(len(text)):
        last_index = find_index(text, pattern, last_index)
        print("last found match at:", last_index)

        if last_index is None:
            break
        
        if last_index >= len(text):
            break

        print("index generated!\n")
        yield last_index


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()