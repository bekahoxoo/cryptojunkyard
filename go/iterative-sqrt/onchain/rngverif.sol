pragma solidity ^0.4.0;

contract rngverif {

    uint256 p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f;
    uint256 prevblock = block.number - 1;
    //uint256 x = uint256(block.blockhash(prevblock));
    uint256 x = 0xfff23423424234234234234ffffffffffff765456898765434567654323ff;
    uint256 crand;

    function verification (uint256 random) returns (bool) {
        for (uint256 i = 1; i < 10; i++) {
            uint256 z;
            z = mulmod(x, x, p);
            x = z;
        }

        if (random == x) {
            crand = random;
            return true;
        }
    return false;
    }
}
