from itertools import permutations

def solve(word): # slow
    with open("/usr/share/dict/words") as words:
        words = words.read().split("\n")
        # brute force the permutations
        perms = permutations(word)

        # check if words are in dictionary
        for perm in perms:
            perm = "".join(perm)
            # print(perm)
            if perm in words:
                return perm

if __name__ == "__main__":
    # while True:
        # word = input("Unscramble a word > ")
        # print(solve(word))

# tnkisesi


# another solution

    test_dict = ["abc", "acb", "cab", "xyz"]

    for word in test_dict:
        print(sum(bytearray(word)))