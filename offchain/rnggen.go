package main

import (
  "math/big"
  "fmt"
  )

func main() {

  p := big.NewInt(0)
  p.SetString("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F", 16)
  /* uncomment to check p = 3 mod 4 (it does)
  four := big.NewInt(4)
  pmod4 := big.NewInt(0)
  pmod4.Mod(p, four)
  fmt.Println(pmod4)
  n := big.NewInt(0)
  n.SetString("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141", 16)
  nmod4 := big.NewInt(0)
  nmod4.Mod(p, four)
  fmt.Println(nmod4)
  */

  // x is the blockhash in our case

  // go's built in ModSqrt already uses tonelli-shanks algo for square rooting
  // it's the currently best know slow generation & fast verification function
  for something {
    y := big.NewInt(0)
    y.ModSqrt(x, p)
  }

  // we're gonna make time for generation vs cost of verification when i'm finished :)

