var timeRequiredToBuy = function(tickets, k) {
  // sol2 74ms 84% 42MB 57%
  let ans = 0; let i = 0;
  while (i <= k) {
    if (tickets[i] < tickets[k]) {
      ans += tickets[i]
    } else {
      ans += tickets[k]
    }
    i += 1
  }
  while (i < tickets.length) {
    if (tickets[i] < tickets[k]) {
      ans += tickets[i]
    } else {
      ans += tickets[k]-1
    }
    i += 1
  }
  return ans
};