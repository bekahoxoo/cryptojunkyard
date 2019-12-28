import secrets

def invert(P):
    (x, y) = P
    return (x, p-y)

def add(P1, P2):
    if P1 == O:
        return P2

    if P2 == O:
        return P1

    if P1 == invert(P2):
        return O

    (x1, y1) = P1
    (x2, y2) = P2

    if P1 == P2:
        m = (3*x1**2 + a) / 2*y1
    else:
        m = (y2 - y1) / (x2 - x1)

    return (m**2 - x1 - x2, m*(x1 - x3) - y1)

def odd(k):
    return k & 1

def scalar_mul(x, k):
    result = O
    while k > 0:
        if odd(k):
            result = add(result, x)
        x = add(x, x)
        k = k >> 1
    return result

class Alice():
    def generate_keypair(self):
        self.secret = secrets.randbelow(r)
        public = scale(G, secret)
        return public

    def compute_secret(self, peer_public):
        return scalar_mul(peer_public, self.secret)

def DHKE():
    alice = Alice()
    bob = Alice()
    A = alice.generate_keypair()
    B = bob.generate_keypair()
    assert alice.compute_secret(B) == bob.compute_secret(A)
    return

def set_curve_0():
    O = (0, 1)
    a = -95051
    b = 11279326
    p = 233970423115425145524320034830162017933
    G = (182, 85518893674295321206118380980485522083)
    r = 29246302889428143187362802287225875743 # = 2^3 * 29246302889428143187362802287225875743
    h = 2**3
    return

def set_curve_1():
    set_curve_0()
    b = 210
    r = 233970423115425145550826547352470124412
    return 

def set_curve_2():
    set_curve_0()
    b = 504
    r = 233970423115425145544350131142039591210
    return 

def set_curve_3():
    set_curve_0()
    b = 727
    r = 233970423115425145545378039958152057148
    return 

def __main__():
    set_curve_0()
    DHKE()

    # All she has to do is find some curves with small subgroups and
    # cherry-pick a few points of small order. Alice will unwittingly compute
    # the shared secret on the wrong curve and leak a few bits of her private
    # key in the process.

    # How do we find suitable curves? Well, remember that I mentioned counting points
    # on elliptic curves is tricky. If you're very brave, you can implement
    # Schoof-Elkies-Atkins. Or you can use a computer algebra system like SageMath.
