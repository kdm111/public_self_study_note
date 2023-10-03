var reverseString = function(s) {
  // sol2 119~154ms 58~22%
  // s.reverse()
  // console.log(s)

  // sol3 88~175ms 93~11%
  // recursive
  var swap = function(left, right){
    if (left < right){
      const temp = s[left]
      s[left] = s[right]; s[right] = temp
      swap(left+1, right-1)
    }
  }
  swap(0, s.length-1)
  console.log(s)

  // sol4 126~138ms 50~37%
  // var left = 0; 
  // var right = s.length-1
  // while (left < right) {
  //   const temp = s[left]
  //   s[left] = s[right]; s[right] = temp
  //   left = left+1; right = right-1
  // }
  // console.log(s)

};

reverseString(["h","e","l","l","o"])