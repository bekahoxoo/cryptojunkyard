I'm not going to pretend I can explain Legrange interpolation better than [this
wolfram alpha
page](http://mathworld.wolfram.com/LagrangeInterpolatingPolynomial.html).

Pretty much we have a bunch of numbers, and we pick a bunch of x coordinates
with y coordinates that please us (1 at x = xi, 0 when x = xj), and then add
the curves that give us these properties, and then we're left with a polynomial
that's uniquely defined by our original bunch of numbers.

Shamir's secret sharing is built from this, with the secret as the result of
the constructed polynomial f evaluted at f(0). There's stuff you can do to make
it more resiliant to adversarial participants (at least, I hope there is).

There's a cute python library using Shamir's secret sharing scheme,
[here](https://github.com/blockstack/secret-sharing). We need to implement this
within the smart contract though. The idea is that people send their signature
_shares_, and together this constructs one signature which verifies correctly.
This signature **is** the random string we desire (for whatever reason that we
desire a random string).
