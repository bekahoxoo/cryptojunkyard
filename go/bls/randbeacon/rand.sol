/* This is BLS and secret sharing as a verifiable randomness beacon!
   Due to the structure of BLS signatures, we can have the 'private key' as a
   secret shared amongst many (n) users, and reform the signature from the
   components that each of these users can produce with their share of the
   secret.

   The aim is to have a 'threshold' signature, with k signature shards
   required, where k < n. This means that rather than the issue of having to
   trust the final user to submit their share, we only need trust one of the
   n - k + 1 remaining parties to behave correctly and submit their share. In
   other words, this assumption translates to the requirement that it is in at
   least one of the remaining parties' interests to actually submit.

   The secret sharing protocol that dfinity uses is called Joint-Feldman
   Verifiable Secret Sharing (JFVSS), and requires an honest majority. */

contract BLSBeacon {

    uint256 public prevSig;

    function BLSBeacon() {
        prevSig = uint256(0000000);
    }

    function HashtoEC(uint256 message) constant returns (uint256 x, uint256 y) {
    /* This is taken from the BLS paper too! :)

    This is a hash function H : {0, 1)* -> G1, so we need G1's equation.
    Each loop will succeed with probability 1/2.

    For reference, with y^2 = f(x), E(Fq) with order m, P in E(Fq) a point with prime order p,
    where p^2 doesn't divide m, G1 = <P>, the algo is:

    1. Given m in {0, 1}* (this just means any length string), set i = 0

    2. Set (x, b) <- H'(i||M) in Fq x {0, 1}.
    (H' is a normal hash function (like sha256), Fq is a field with order q
    (we'd mod q for sha256), b is a bit.)

    3. If f(x) is a quadratic residue (which would mean some y exists st y^2 = f(x)),

      3a. Let y0, y1 in Fq be the two square roots of f(x).
      Use b to choose between these roots.
      Choose some full ordering of Fq and ensure y1 > y0 according to this ordering
      (swapping y0 and y1 if necessary). Set P̃M in E(Fq) to be the point P̃M = (x, yb).

      3b. Compute PM = (m/p) P̃M. Then PM is in G1 . If PM = O, go to step 4.
      Otherwise, return PM.

    4. i = i + 1, go to step 2. */

    uint256 message = prevSig;
    uint256 i = 0;

	// Security parameter. P(fail) = 1/(2^k)
	uint k = 10;
	uint256 z = fieldOrder + 1;
	z = z / 4;

	for (uint i = 0; i < k; i++) {

		h = sha256(i, message) % fieldOrder;
		x = h % fieldOrder;
		b = h % 2;

		// secp256k1's equation
		uint256 beta = addmod(mulmod(mulmod(x, x, fieldOrder), x, fieldOrder), 7, fieldOrder)    ;
		y = expmod(beta, z, fieldOrder);
		if (beta == mulmod(y, y, fieldOrder)) {
			return (x, y);
		}
	}

}

function SigCombine() {
    /* We have that the initial message is some random seed, then the following
    messages are the output of the previous threshold signature.
    So m = prevCombinedSig */

}

}
