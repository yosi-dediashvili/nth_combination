def nth_combination(start_combination, combination_options, n_value):
    """
    Calculate the N-th combination of a string. The function does not evaluate
    n combination before outputing the n combination. The function acts upon
    the combination as a "natural number" with radix equals to the number of 
    combination_options characters.

    For example, for combination_options = "abc", our base is 3. The representation
    is LSB aligned (The left char is the 

    start_combination is the starting point for the combination. All the items
    within this combination must be within the combination_options space.

    combination_options is the range from which the combination is constructed.

    n_value is the combination index relative to the start_combination value.

    The output of the function is the nth_combination. The combination string 
    length is identical to the length of start_combination.
    """
    radix = len(combination_options)
    new_combination = [""] * len(start_combination) # Will store the result.
    remainder_temp = remainder = n_value
    # For each char.
    for i in range(len(start_combination)):
        c_i = start_combination[i]
        c_idx = combination_options.find(c_i)
        remainder_temp = (c_idx + remainder) / radix
        n_idx = (c_idx + remainder) % radix
        remainder = remainder_temp
        new_combination[i] = combination_options[n_idx]
    return ''.join(new_combination)

test_combs = \
    [("aaaa", "ab",     6,      "abba"),
     ("aaaa", "abc",    34,     "bcab"),
     ("aaaa", "abc3",   190,    "c33c"),
     ("aaaa", "abc3",   256,    "aaaa"),
     ("aaaa", "abc3",   255,    "3333"),
     ("aaaa", "abc3",   270,    "c3aa")]

def test():
    for comb in test_combs:
        print "------------------------------------------"
        print "start_combination: %s, combination_options: %s" % (comb[0], comb[1])
        res = nth_combination(comb[0], comb[1], comb[2])
        print "nth_combination[%s]: %s" % (comb[2], res)
        if res != comb[3]:
            raise Exception("Wrong Combination [%s] !!!" % comb[3])

if __name__ == '__main__':
    test()
