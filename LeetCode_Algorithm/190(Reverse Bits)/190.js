var reverseBits = function(n) {
    // sol1 127ms 18%
    let ans = 0; let pow = 32
    while (pow > 0)
    {
        ans *= 2;
        ans += (n & 1);
        n = n >> 1
        pow -= 1
    }
    return ans
};