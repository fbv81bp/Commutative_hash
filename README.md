# Commutative_hash
### A commutative hash, that relies on modexp powered permutations and modular sums that should hinder solving the discrete logarithm problem.

Exponents by a smaller primes over the modulus of one larger prime create such permutations that may be shuffled.

Simply using a shuffle of such permutations would just result in one equal permutation, whose exponent would be the product of all exponents that resulted the sub-permutations.

These sub-permutations are 'compatible' in a sense, that no matter what, however we shuffle the very same set of permutations, the outcome always remains the same. Because of this IFF the discrete logarithm problem can be solved someday, such a series of permutations is not safe on its own by itself.

However, since addition is commutative, we may sum up outputs of parallel layers of these permutations, in order to hinder tracing back based on the final output, what exponent should be equal to the product of exponents inbetween, so preventing this way to calculate the discrete logarithm is vital.

Summing up the core idea is, that modular exponentiation is treated as an index function to an array, and multiple rounds of such permutations are applied one after the other, while inbetween the layers of permutations, the array values are summed up over a modulus, to hinder tracing back the individual permutations. (Which would be very easy if a discrete logarithm could determine their endproduct from the final series of outputs.)
