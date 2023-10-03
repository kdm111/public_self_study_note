var removeDuplicates = function(s) {
  // sol1 118~186ms 55~18%
  // stack = []
  // for (let c of s){
  //   if (stack.length != 0 && stack[stack.length-1] == c){
  //     stack.pop()
  //   }
  //   else{
  //     stack.push(c)
  //   }
  // }
  // return stack.join("")


  // sol2 O(n^2), O(1) 시간초과
  duplicates = []
  for(let c=0; c < 26; c++){
    let chr = String.fromCharCode(97+c); chr += chr
    duplicates.push(chr)
  }
  prevLength = -1
  while (prevLength != s.length){
    prevLength = s.length
    for (let c of duplicates){
      s = s.replace(c, "")
    }
  }
  return s
};

console.log(removeDuplicates("abccbf"))