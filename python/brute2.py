import itertools
def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=i)
        for i in range(1, maxlength + 1)))

print list(bruteforce('abcdefghijklmnopqrstvwxyz', 3))
