import itertools

def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=i)
        for i in range(maxlength, maxlength + 1)))
count = 0
for i in  bruteforce('abcde', 4):
	print i
