import itertools

def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=i)
        for i in range(1, maxlength + 1)))
count = 0
for i in bruteforce('abcdefghijklmnopqrstvwxyzABCDEFGHIJKLMNOPQRSTVW1234567890', 4):
	count += 1
print count