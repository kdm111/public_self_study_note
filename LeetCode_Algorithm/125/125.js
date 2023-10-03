var isPalindrome = function(s) {
  // sol1 84~86 79~76%
  // ascii code
  // var string = ""
  // for (let left=0; left < s.length; left++){
  //   // process.stdin.write(s[left].charCodeAt() + " ")
  //   let asciiCode = s[left].charCodeAt()

  //   if ( 65 <= asciiCode  && asciiCode <= 90){
  //     string += s[left].toLowerCase()
  //   }
  //   if (97 <= asciiCode && asciiCode <= 122){
  //     string += s[left]
  //   }
  //   if (48 <= asciiCode && asciiCode <= 57){
  //     string += s[left]
  //   }  
  // }
  
  // for (let left=0; left < parseInt(string.length/2); left++){
  //   if (string[left] != string[string.length-1-left]){
  //     return false
  //   }
  // }
  // return true


  // sol2 64~110 99~47%보다 빠름
  // var s = s.toLowerCase().split('')
  // var string = s.filter((chr)=>{
  //   if(isalnum(chr)){
  //     return true
  //   }
  // })
  // let right = string.length
  // for (let left=0; left < parseInt(string.length/2); left++){
  //   if (string[left] != string[right-left-1]){
  //     return false
  //   }
  // }
  // return true

  // sol3 89~99ms 72~61%보다 빠름
  // while을 사용해서 조금 더 깔끔함
  var left = 0
  var right = s.length-1

  while (left < right){
    while (left < right && !isalnum(s[left])){
      left += 1
    }
    while (left < right && !isalnum(s[right])){
      right -= 1
    }
    if (s[left].toLowerCase() != s[right].toLowerCase()){
      return false
    }
    left += 1
    right -= 1
  }

  return true

};
function isalpha(chr){
  return (((chr >= 'a') && (chr <= 'z')) || ((chr >= 'A') && (chr <= 'Z')))
}
function isdigit(chr){
  return ((chr >= '0') && (chr <= '9'))
}
function isalnum(chr){
  return ( isalpha(chr) || isdigit(chr) )
}

console.log(isPalindrome("A p P a"))
