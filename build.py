from itertools import chain, combinations

def powerset(iterable):

    xs = list(iterable)
    # note we return an iterator rather than a list
    return chain.from_iterable(combinations(xs,n) for n in range(len(xs)+1))



# what is input? (2,3,4)
# what should be the output? () (2) (3 ) (4) (2,3) (2,4) (3,4) (2,3,4)
