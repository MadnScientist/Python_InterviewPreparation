import itertools
import time

def lcs(l, l2):
    start_time = time.time()
    s1 = set(list(l))
    s2 = set(list(l2))

    sol = s2.intersection(s1)

    for val in itertools.permutations(sol): 
        if ('').join(val) in l or ('').join(val) in l2:
            sol = val
            break

    
    print("--- %s seconds ---" % (time.time() - start_time))
    return len(sol)

l = "AGGTAB"
l2 = "GXTXAYB"
lcs(l, l2)