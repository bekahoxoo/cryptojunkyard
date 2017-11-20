/* This is actually very simple when pairing checks exist.

h = H(m) with m the message to be signed

Sanity checks for h, h^x in G1 and g2, g2^x (= v) in G2 will be skipped for now.
We could check they're all mod p (given below) but if they aren't the check will fail anyway.

All we actually need to do is check e(h^x, g2) = e(h, g2^x),
with v = g2^x, and sigma = h^x, e(sigma, g2) = e(h, v)

Elements of G1 are (x, y), both 256 bit elements of F_q; and elements of G2 are (x + iy, a + ib),
so 4 256 elements on F_q^2, with order
p = 21888242871839275222246405745257275088696311157297823662689037894645226208583

Security relies on aCDH (watch this cool video ;) https://youtu.be/F4x2kQTKYFY?t=37m46s)
*/

contract BLSVerif {

  // g2 has to be the same generator of G2 as is used in the signature gen algo.
  // specified by 4 uint256s that are used to form (x + iy, a + ib)
  uint256 g2xa = 11559732032986387107991004021392285783925812861821192530917403151452391805634;
  uint256 g2xb = 10857046999023057135944570762232829481370756359578518086990519993285655852781;
  uint256 g2ya = 4082367875863433681332203403145435568316851327593401208105741076214120093531;
  uint256 g2yb = 8495653923123431417604973247489272438418190587263600148770280649306958101930;

  function Verif(uint256 sigmax, uint256 sigmay, uint256 hx, uint256 hy,
                  uint256 vxa, uint256 vxb, uint256 vya, uint256 vyb) public returns (bool) {

      // using the pairing check precompile at address 8
      // do we assume non-degenerate? non-zero? yeah? :)
      if (pairingcheck((sigmax, sigmay, g2xa, g2xb, g2ya, g2yb), (hx, hy, vxa, vxb, vya, vyb))) {
          return true;
      }
      else return false;
  }
  
}
