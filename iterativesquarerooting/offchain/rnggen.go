package main

import (
  "math/big"
  "fmt"
  )

func main() {

  p := big.NewInt(0)
  p.SetString("fffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f", 16)
  /* uncomment to check p = 3 mod 4 (it does)
  four := big.NewInt(4)
  pmod4 := big.NewInt(0)
  pmod4.Mod(p, four)
  fmt.Println(pmod4)
  */

  x := big.NewInt(0)
  x.SetString("fff23423424234234234234ffffffffffff765456898765434567654323ff", 16)
  // this should be for i < some set parameter making computation take 60 seconds :(
  for i := 0; i < 10; i++ {
  // x is the blockhash in our case
  // go's built in ModSqrt already uses tonelli-shanks algo for square rooting
  // it's the currently best know slow generation & fast verification function
    z := big.NewInt(0)
    z.ModSqrt(x, p)
    x = z
    fmt.Println(x)
  }

  // we're gonna make time for generation vs cost of verification when i'm finished :)
}
