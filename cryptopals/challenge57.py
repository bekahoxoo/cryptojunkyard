from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from modint import chinese_remainder
from functools import reduce
import secrets
import hashlib

from functools import reduce
def chinese_remainder(n, a):
    ssum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        pp = prod // n_i
        ssum += a_i * mul_inv(pp, n_i) * pp
    return ssum % prod
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
 
 
def aes_encrypt(msg, key, iv):
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return cipher.encrypt(pad(msg, AES.block_size))

def cbc_mac(msg, key, iv):
    mac = aes_encrypt(msg, key, iv)
    return mac.hex()[-(AES.block_size * 2):]

iv = bytes(16)
msg = b"alert('MZA who was that?');\n"
key = b"YELLOW SUBMARINE"
assert cbc_mac(msg, key, iv) == "296b8d7cb78a243dda4d0a61d33bbdd1"

class Alice():
    def __init__(self, p, g, q):
        self.p = p
        self.g = g
        self.q = q

    def pk_set(self, a, A):
        self.a = a
        self.A = A
        return

    def pk_gen(self):
        self.a = secrets.randbelow(self.q)
        self.A = pow(self.g, self.a, self.p)
        return

    def send_params(self):
        return self.p, self.g, self.q

    def send_pk(self):
        return self.A

    def verify_b_msg(self, m):
        self.B, msg, mac, iv = m
        self.s = pow(self.B, self.a, self.p)
        kk = self.s.to_bytes(65, byteorder='big')
        key = hashlib.sha256(kk).hexdigest()[:16]
        mm = cbc_mac(key + msg, key, iv)
        assert mac == mm
        return

    def evil_verify_b_msg(self, h, m, maxk):
        self.B, msg, mac, iv = m
        for k in range(maxk):
            self.s = pow(h, k, self.p)
            kk = self.s.to_bytes(65, byteorder='big')
            key = bytearray.fromhex(hashlib.sha256(kk).hexdigest())[:16]
            mm = cbc_mac(key + msg, key, iv)
            if mac == mm:
                return k
        return



class Bob():
    # Receive p, g, q
    def receive_params(self, msg):
        p, g, q = msg
        self.p = p
        self.g = g
        self.q = q
        return

    def pk_gen(self):
        self.b = secrets.randbelow(self.q)
        self.B = pow(self.g, self.b, self.p)
        return

    def receive_pk(self, A):
        self.A = A
        return

    # B->A
    # Send B, msg, mac, iv
    def send_b_msg(self):
        self.s = pow(self.A, self.b, self.p)
        kk = self.s.to_bytes(65, byteorder='big')
        key = bytearray.fromhex(hashlib.sha256(kk).hexdigest())[:16]
        iv = bytes(16)
        msg = b'crazy flamboyant for the rap enjoyment'
        mac = cbc_mac(key + msg, key, iv)
        return self.B, msg, mac, iv

# Pohlig-Hellman algorithm for discrete logarithms
def step_one():
    i = secrets.randbelow(len(f))
    r = f[i]
    rr = secrets.randbelow(p - 1) + 1
    h = pow(rr, (p - 1)//r, p)
    if h == 1:
        return step_one()
    return h, r

def step_two(h, r):
    eve.pk_set(0, h)
    bob.receive_pk(eve.send_pk())
    return

def step_three():
    msg = bob.send_b_msg()
    print(msg)
    return msg

def step_four(h, r, msg):
    kmodr = eve.evil_verify_b_msg(h, msg, r)
    return kmodr

def step_five():
    veck = []
    vecr = []
    product = 1
    for i in range(len(f)):
        h, r = step_one()
        step_two(h, r)
        msg = step_three()
        kmodr = step_four(h, r, msg)
        veck.append(kmodr)
        vecr.append(r)
        product *= r
        if product > q:
            print(veck)
            print(vecr)
            return chinese_remainder(vecr, veck)
    return

p = 7199773997391911030609999317773941274322764333428698921736339643928346453700085358802973900485592910475480089726140708102474957429903531369589969318716771
g = 4565356397095740655436854503483826832136106141639563487732438195343690437606117828318042418238184896212352329118608100083187535033402010599512641674644143
q = 236234353446506858198510045061214171961
j = 30477252323177606811760882179058908038824640750610513771646768011063128035873508507547741559514324673960576895059570

def factor_upto(j, n=16):
    factors = []
    for i in range(3, 2**n):
        if (j % i == 0) and (j % i**2 != 0):
            factors.append(i)
    return factors

f = factor_upto(j)

eve = Alice(p, g, q)
bob = Bob()
bob.receive_params(eve.send_params())
bob.pk_gen()

print(step_five())
