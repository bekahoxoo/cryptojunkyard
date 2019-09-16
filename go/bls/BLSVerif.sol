/* This is actually very simple when pairing checks exist.

h = inverse(H(m)), with m the message to be signed

Sanity checks for h, h^x in G1 and g2, g2^x (= v) in G2 will be skipped for now.
We could check they're all mod p (given below) but if they aren't the check will fail anyway.

All we actually need to do is check e(h^x, g2) = e(h, g2^x),
with v = g2^x, and sigma = h^x, e(sigma, g2) = e(h, v)

The precompile tests that e(a, b) = e(-c, d), so we need to send the ***inverse*** of H(m).

Elements of G1 are (x, y), both 256 bit elements of F_q; and elements of G2 are (x + iy, a + ib),
so 4 256 elements on F_q^2, with order
p = 21888242871839275222246405745257275088696311157297823662689037894645226208583

Security relies on aCDH (ref: https://youtu.be/F4x2kQTKYFY?t=37m46s)
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
      if (pairingcheck(sigmax, sigmay, g2x, g2y, g2a, g2b, hx, hy, vx, vy, va, vb)) {
          return true;
      }
      else return false;
  }

  // i should really be using arrays what am I doing
  function pairingcheck(uint256 ax, uint256 ay, uint256 bx, uint256 by, uint256 ba, uint256 bb,
                        uint256 cx, uint256 cy, uint256 dx, uint256 dy, uint256 da, uint256 db)
                        returns (bool output) {

      uint256[12] memory input;
      input[0] = ax;
      input[1] = ay;
      input[2] = bx;
      input[3] = by;
      input[4] = ba;
      input[5] = bb;
      input[6] = cx;
      input[7] = cy;
      input[8] = dx;
      input[9] = dy;
      input[10] = da;
      input[11] = db;

      assembly {
        // call precompile
        let success := call(sub(gas, 2000), 0x08, 0, input, 0x0180, output, 0x20)
        // gas fiddling
        switch success case 0 {
          revert()
        }
      }
      return output;

}
