mods = [65537]#[991, 1117, 1279]

pows = [\
179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,\
283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,\
419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,\
547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,\
661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809]

candidates = []
groups = []
for m in mods:
    for p in pows:
        base = 19
        exps = []
        while base not in exps:
            exps.append(base)
            base = pow(base, p, m)
        if len(exps) == 4096:
            candidates.append(p)
            groups.append(exps)

print(candidates)
print(len(groups))

filtered = []
testl = []
for g in groups:
    test = True
    for e in g:
        if e not in groups[0]:
            test = False
    testl.append(test)
    if test:
        filtered.append(g)
print(len(filtered), testl)

perms = [[i for i in range(4096)]]
for f in filtered[1:]:
    perm = []
    for e in f:
        perm.append(filtered[0].index(e))
    perms.append(perm)

#print(perms)

from copy import deepcopy
def shuffle(din, keys):
    donut = deepcopy(din)
    for k in range(len(keys)):
        din = deepcopy(donut)
        for d in range(len(din)):
            donut[perms[k][d]] += din[d]
            donut[perms[k-2][d]] += din[d]
            donut[perms[k-11][d]] += din[d]
    return(donut)

'''
from random import randint as rdi
keylength = 5 # test value for dispersion testing
keyring = [3,5,6,8,11]
seed = [0 for i in range(4096)]
seed[39] = 1
seed_out = shuffle(seed, keyring)
'''

from random import randint as rdi
test_results = []
for test_run in range(4096):

    keylength = 12 # test value for dispersion testing
    keyring = [rdi(0,11) for _ in range(keylength)]

    seed = [1 if test_run == i else 0 for i in range(4096)]
  
    seed_out = shuffle(seed, keyring)
    
    affected = 0
    afflist = []
    for so in seed_out:
        if so > 0:
            affected += 1
            afflist.append(so)
    test_results.append([affected, test_run]) # , afflist])

#print()
#print(test_results)
test_results.sort()
print()
print(test_results)
print()

