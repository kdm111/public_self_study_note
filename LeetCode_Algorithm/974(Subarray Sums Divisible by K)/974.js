var subarraysDivByK = function(nums, k) {
  // sol1 82ms 97% 46.4MB 86%
  let ans = 0; let total = 0
  let cntArr = Array(k).fill(0); cntArr[0] = 1
  for (let num of nums) {
    total += num; total %= k
    // 모듈러 연산의 나머지는 음수가 될 수 없다. 따라서 +k로 양수로 바꾸어준다.
    if (total < 0) {total += k} 
    ans += cntArr[total]
    cntArr[total] += 1
  }
  return ans
};
// -2 == 5 * 0 - 2
// -2 == 5 * -1 + 3