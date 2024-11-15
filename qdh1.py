mods = [65537] #[991, 1117, 1279]

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

from random import randint as rdi
keylength = 24
keyringA = [rdi(0,11) for _ in range(keylength)]
keyringB = [rdi(0,11) for _ in range(keylength)]
seed = [rdi(0,16) for _ in range(4096)]
    
from copy import deepcopy
def shuffle(din, keys):
    donut = deepcopy(din)
    for k in range(len(keys)):
        din = deepcopy(donut) # correction: line was missing; seed's dispersion gets avelanche effect this way
        for d in range(len(din)):
            donut[perms[keys[k]][d]] += din[d] # corrections: keys[] were missing... ;)
            donut[perms[keys[k-2]][d]] += din[d]
            donut[perms[keys[k-11]][d]] += din[d]
            donut[perms[keys[k]][d]] %= 17
            donut[perms[keys[k-2]][d]] %= 17
            donut[perms[keys[k-11]][d]] %= 17
    return(donut)

print(shuffle(shuffle(seed, keyringA), keyringB) == shuffle(shuffle(seed, keyringA), keyringB))

for p in perms:
    print(p[0:15])


