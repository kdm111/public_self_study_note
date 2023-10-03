var getHint = function(secret, guess) {
  // 136ms 21%
  sArr = new Array(10).fill(0)
  gArr = new Array(10).fill(0)
  let bull = 0 
  for (let idx=0; idx < secret.length; idx++){
    if(secret[idx] == guess[idx]) {
      bull += 1
    } 
    else {
      sArr[parseInt(secret[idx])] += 1
      gArr[parseInt(guess[idx])] += 1
    }
  }
  let cow = 0
  for (let i=0; i < 10; i++) {
    cow += Math.min(sArr[i], gArr[i])
  }
  return String(bull) + 'A' + String(cow) + 'B'
};

console.log(getHint("1807", "7810"))