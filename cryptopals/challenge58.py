def fp(y, k, p):
    return pow(2, y % k, p)

class Kangaroos():

    def __init__(self, a, b, g, p, k, N):
        self.a = a
        self.b = b
        self.g = g
        self.p = p
        self.k = k # k = step size
        self.N = N # N = number of steps

    def f(self, y):
        return pow(2, y % self.k, self.p)

    def tame_kangaroo(self):
        xT = 0
        yT = pow(self.g, self.b, self.p)
        for i in range(self.N):
            xT = xT + roo.f(yT)
            yT = yT * pow(self.g, roo.f(yT), self.p)
        return xT, yT

    def wild_kangaroo(self, xT, yT, y):
        xW = 0
        yW = y

        while xW < b - a + xT:
            xW = xW + roo.f(yW)
            yW = yW * pow(self.g, roo.f(yW), self.p)

            if yW == yT:
                return b + xT - xW
        return None

if __name__ == '__main__':
    # [a, b] is the range that the discrete log, x, of y, will lie in
    p = 11470374874925275658116663507232161402086650258453896274534991676898999262641581519101074740642369848233294239851519212341844337347119899874391456329785623
    q = 335062023296420808191071248367701059461
    j = 34233586850807404623475048381328686211071196701374230492615844865929237417097514638999377942356150481334217896204702
    g = 622952335333961296978159266084741085889881358738459939978290179936063635566740258555167783009058567397963466103140082647486611657350811560630587013183357

    k = 30
    # N is then derived from f - take the mean of all possible outputs of f and
    # multiply it by a small constant, e.g. 4.
    outs = [fp(y, k, p) for y in range(k)]
    N = sum(outs)//len(outs) * 4

    # x in range [0, 2^20]
    a = 0
    b = 2**20
    roo = Kangaroos(a, b, g, p, k, N)
    y0 = 7760073848032689505395005705677365876654629189298052775754597607446617558600394076764814236081991643094239886772481052254010323780165093955236429914607119
    xo, yo = roo.tame_kangaroo()
    x0 = roo.wild_kangaroo(xo, yo, y0)
    print(x0) 
    assert pow(g, x0, p) == y0
    
    # x in range [0, 2^40]
    a = 0
    b = 2**40
    roo = Kangaroos(a, b, g, p, k, N)
    y1 = 9388897478013399550694114614498790691034187453089355259602614074132918843899833277397448144245883225611726912025846772975325932794909655215329941809013733
    xi, yi = roo.tame_kangaroo()
    x1 = roo.wild_kangaroo(xi, yi, y1)
    print(x1) 
    assert pow(g, x1, p) == y1

