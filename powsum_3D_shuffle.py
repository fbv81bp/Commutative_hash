'''
Using a 36x36x36 3D state and shuffling it in all 3 dimensions before summing up 3 different permutations per layer.
'''

from random import randint as rdi

base = 37 # modulus of permutations by indexing with modexp 
exps = [3,5,7,11,13,17,19,23,29,31] # exponents of permutations by indexing with modexp, indexed by key material

# 10*32 possible different keys
keylength = 32
keyAlice = [rdi(0,9) for _ in range(keylength)]
keyBobba = [rdi(0,9) for _ in range(keylength)]

# state is 46656 bytes size
seed = [[[rdi(0,255) for _ in range(base)] for _ in range(base)] for _ in range(base)]

# creating 3 shuffled versions of the previous state to be summed up next7
# shuffling happens in all three dimensions and with up to 9 different permutations (depending on key portions being different)
# offsets were choosen arbitrarily
def shuffle(seed, keys, keyindex):
    donut = []
    donut.append([[[seed[i ** exps[keys[keyindex    ]] % base][j ** exps[keys[keyindex - 1]] % base][k ** exps[keys[keyindex - 2]] % base] \
        for i in range(base)] for j in range(base)] for k in range(base)])
    donut.append([[[seed[i ** exps[keys[keyindex - 3]] % base][j ** exps[keys[keyindex - 5]] % base][k ** exps[keys[keyindex - 7]] % base] \
        for i in range(base)] for j in range(base)] for k in range(base)])
    donut.append([[[seed[i ** exps[keys[keyindex - 4]] % base][j ** exps[keys[keyindex - 8]] % base][k ** exps[keys[keyindex - 9]] % base] \
        for i in range(base)] for j in range(base)] for k in range(base)])
    return donut

# summing up the 3 different permutations of an intermediate state
def sumup(shuffle):
    return [[[(shuffle[0][i][j][k] + shuffle[1][i][j][k] + shuffle[2][i][j][k]) % 256 \
        for i in range(base)] for j in range(base)] for k in range(base)]

# hashing by permuting the state to 3 diverse versions and then summing those up repeatedly, based on key material length
def hashing(seed, keys):
    for keyindex in range(len(keys)):
        seed = sumup(shuffle(seed, keys, keyindex))
    return seed

# testing Diffie-Hellman protocol
print(hashing(hashing(seed, keyBobba), keyAlice) == hashing(hashing(seed, keyAlice), keyBobba)) # passed: True
