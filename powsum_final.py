'''
Exponents by a smaller primes over the modulus of one larger prime create such permutations that may be shuffled.
sum
Simply using a shuffle of such permutations would just result in one equal permutation, whose exponent would be the product of all exponents that resulted the sub-permutations.

These sub-permutations are 'compatible' in a sense, that no matter what, however we shuffle the very same set of permutations, the outcome always remains the same. Because of this IFF the discrete logarithm problem can be solved someday, such a series of permutations is not safe on its own by itself.

However, since addition is commutative, we may sum up outputs of parallel layers of these permutations, in order to hinder tracing back based on the final output, what exponent should be equal to the roduct of exponents inbetween, preventing this way to calculate the discrete logarithm.

Summing up the core idea is, that modular exponentiation is treated as an index function to an array, and multiple rounds of such permutations are applied one after the other, while inbetween the layers of permutations, the array values are summed up over an modulus, to hinder tracing back the individual permutations. (Which would be very easy if a discrete logarithm could determine their endproduct from the final series of numbers.)
'''

from random import randint as rdi

for testing in range(10):

    keylength = 24 # 24 => 2x192 bit key material
    keyAlice = [rdi(0,15) for _ in range(keylength)] # set of 4 bit subkeys, which will be used to index...
    keyBobba = [rdi(0,15) for _ in range(keylength)] # ...the exponent set, creating a shuffle of permutations

    seed = [rdi(0,255) for _ in range(256)] # random seed used to initialize the Diffie-Hellman protocol

    def Black_shuffle(data, keys): # proof of concept for a hash-like compression function with commutative property, so that it can be used in the DH key exchange
        exps = [113,127,131,139,157,163,167,179,181,191,199,223,229,233,239,241] # set of exponents that are used to create 'compatible' permutations
        base = 257
        for k in range(len(keys)): # rounds of using key material to select diverse permutations
            donut = []
            for d in range(len(data)):
                donut.append( (data[d**exps[keys[k]]% base] + data[d**exps[keys[k-1]]%base]) % 256) # elementwise sums of pairs of compatible permutations in every round
        return(donut)

    print("Alice's key:", keyAlice)
    print("Bobba's key:", keyBobba)
    print("Seed:", seed[0:4], "...")
    print("Alice's result:", Black_shuffle(Black_shuffle(seed, keyAlice), keyBobba)[0:4], "...") # Diffie-Hellman protocol based key exchange
    print("Bobba's result:", Black_shuffle(Black_shuffle(seed, keyBobba), keyAlice)[0:4], "...") # Diffie-Hellman protocol based key exchange
    # Test for equality:
    print(Black_shuffle(Black_shuffle(seed, keyBobba), keyAlice) == Black_shuffle(Black_shuffle(seed, keyAlice), keyBobba))