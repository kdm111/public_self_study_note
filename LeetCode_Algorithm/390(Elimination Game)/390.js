var lastRemaining = function(n) {
  // sol1 141ms 78% 45.4MB 96%
  let left = true; let head = 1; let move = 1
  while (n > 1) {
    if (left || n % 2 == 1) {
      head += move
    }
    move *= 2
    left = !left
    n = parseInt(n / 2)
  }  
  return head
};
console.log(lastRemaining(5))