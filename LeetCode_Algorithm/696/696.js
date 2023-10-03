var countBinarySubstrings = function(s) {
  // sol1 O(n), O(n) 72~80ms 93~83%
  // var curr = 1;
  // var counts = [] 
  // for (let idx=1; idx<s.length; idx++){
  //   if (s[idx-1] != s[idx]){
  //     counts.push(curr)
  //     curr = 1
  //   }
  //   else{
  //     curr += 1
  //   }
  // }
  // counts.push(curr)

  // var ans = 0
  // for (idx=1; idx < counts.length; idx++){
  //   ans += Math.min(counts[idx-1], counts[idx])
  // }
  // return ans


  // sol2 O(n), O(1)
  var ans = 0; var prev = 0; var curr = 1;
  for (let idx=1; idx < s.length; idx++){
    if (s[idx-1] != s[idx]){
      ans += Math.min(prev, curr)
      prev = curr; curr = 1
    }else{
      curr += 1
    }
    console.log(ans)
  }
  return ans+Math.min(prev, curr)

};

console.log(countBinarySubstrings("1100"))