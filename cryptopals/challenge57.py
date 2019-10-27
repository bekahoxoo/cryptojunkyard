class Alice():
    def __init__(self, p, g, q):
        self.p = p
        self.g = g
        self.q = q
        self.a = secrets.randbelow(self.q)
        self.A = pow(self.g, self.a, self.p)

    # A->B
    # Send "p", "g", "A"
    def send_a_msg(self):
        return self.p, self.g, self.A

    # Receive AES-CBC(SHA1(s)[0:16], iv, msg) + iv for some iv, msg chosen by Bob
    def recieve_b_msg(self, msg):
        self.B, cph, iv = msg
        return msg

    def decrypt_b_msg(self, msg):
        self.B, cph, iv = msg
        cipher = aes_from_secret(self.s, iv)
        msg = cipher.decrypt(cph)
        print(msg)
        return msg

class Bob():
    # Receive "p", "g", "q", "A"
    def recieve_a_msg(self, msg):
        p, g, q, A = msg
        self.p = p
        self.g = g
        self.q = q
        self.A = A
        self.b = secrets.randbelow(self.q)
        self.B = pow(self.g, self.b, self.p)
        return

    # B->A
    # Send "B"
    # Send AES-CBC(SHA1(s)[0:16], iv=random(16), msg) + iv
    def send_b_msg(self):
        iv = secrets.token_bytes(16)
        cipher = aes_from_secret(self.s, iv)
        m = b'crazy flamboyant for the rap enjoyment'
        mac =  
        return self.B, cph, iv

# could also have eve feed these into functions..?
p = 7199773997391911030609999317773941274322764333428698921736339643928346453700085358802973900485592910475480089726140708102474957429903531369589969318716771
g = 4565356397095740655436854503483826832136106141639563487732438195343690437606117828318042418238184896212352329118608100083187535033402010599512641674644143
# q = order of g => g^q = 1 mod p.
q = 236234353446506858198510045061214171961

alice = Alice(p, g, q)
bob = Bob()
bob.recieve_a_msg(alice.send_a_msg())
alice.recieve_b_msg(bob.send_b_msg())


# the fact that q divides p-1 guarantees the existence of
# elements of order q. What if there are smaller divisors of p-1?
# find factors of j smaller than 2**16 (skip repeated factors)
# j * q = p - 1. j has lots of small factors
j = 30477252323177606811760882179058908038824640750610513771646768011063128035873508507547741559514324673960576895059570

def factor_upto(n=16):
    factors = []
    for i in range(2**n):
        if (j % i == 0) and (j % i**2 != 0):
            factors.append(i)
    return factors

f = factor_upto()
print(len(f))

# Pohlig-Hellman algorithm for discrete logarithms

# 1. Take one of the small factors j. Call it r. We want to find an element h
# of order r. To find it, do:
# h := rand(1, p)^((p-1)/r) mod p
# If h = 1, try again.

def step_one():
    i = secrets.randbelow(len(f))
    r = f[i]
    rr = secrets.randbelow(p)
    h = pow(rr, (p - 1)//r, p)
    if h == 1:
        return step_one()
    return h, r

# 2. You're Eve. Send Bob h as your public key. Note that h is not a valid
# public key! There is no x such that h = g^x mod p. But Bob doesn't know that.
h, r = step_one()
eve = Alice()
bob.receive_a_msg((p, g, h)) # why are there no x st h = g^x mod p? is h > q? or in a different subgroup!

# 3. Bob will compute:
# K := h^x mod p
# Where x is his secret key and K is the output shared secret. Bob then sends
# back (m, t), with:
# m := "crazy flamboyant for the rap enjoyment"
# t := MAC(K, m)
msg = eve.receive_b_msg(bob.send_b_msg())

# 4. We (Eve) can't compute K, because h isn't actually a valid public key. But
# we're not licked yet.
# Remember how we saw that g^x starts repeating when x > q? h has the same
# property with r. This means there are only r possible values of K that Bob
# could have generated. We can recover K by doing a brute-force search over these
# values until t = MAC(K, m).
# Now we know Bob's secret key x mod r.
def step_four(h, r, mac):
    return

# 5. Repeat steps 1 through 4 many times. Eventually you will know:
# x = b1 mod r1 x = b2 mod r2 x = b3 mod r3 ...  Once (r1 * r2 * ... * rn) > q,
# you'll have enough information to reassemble Bob's secret key using the Chinese
# Remainder Theorem.
