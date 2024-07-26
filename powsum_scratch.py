from random import randint as rdi


keylength = 1 # 24 => 192 bit keying
keyAlice = [rdi(0,15) for _ in range(keylength)]
keyBobba = [rdi(0,15) for _ in range(keylength)]

data = [rdi(0,255) for _ in range(16)]

def shuffle(data, keys):
    exps = [113,127,131,139,157,163,167,179,181,191,199,223,229,233,239,241]
    base = 17
    for k in range(len(keys)):
        donut = []
        for d in range(len(data)):
            donut.append(data[d**exps[keys[k]]% base])
        dout = []
        for i in range(len(donut)):
            # contains a circular rotation, which is not compatible with the interchangeble permutations of modular exponents:
            dout.append((donut[i-1] + donut[i])%256) 
    return(dout)

print(shuffle(shuffle(data, keyAlice), keyBobba))
print(shuffle(shuffle(data, keyBobba), keyAlice))
