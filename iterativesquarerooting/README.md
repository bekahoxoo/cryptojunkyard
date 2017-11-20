# p2prng

- Randomness beacon for eth.
- Requires 1 communication => 1 honest user out of everyone with a view of eth

Motivation and protocol design described
[here](https://medium.com/@rmercer/p2prngs-teasing-randomness-from-blockchains-43a9b615a4cb),
[here](https://medium.com/@rmercer/p2prng-v2-still-teasing-randomness-from-blockchains-6d102dbab4d6)
and
[here](https://medium.com/@rmercer/p2prng-teasing-randomness-from-blockchains-v3-ffbb77cfd740).

In brief, we feed blockhashes into a function that takes sufficiently long to
compute that any miner that tries to compute the output of the blockhash (for
example, to determine whether or not they will receive money due to the
outcome) will forfeit the block. This forfeit is _implicit_ in the ethereum
mining protocol, as we rely only on the assumption that in the time it takes
for a dishonest miner to computer the outcome, an honest miner will have
submitted an unchecked block.
