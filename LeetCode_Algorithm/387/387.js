var firstUniqChar = function(s) {

  // sol1 101~130 87~65%보다 빠름
  // var hashMap = {}
  // for (let i=0; i < s.length; i++){
  //   if(hashMap[s[i]] == undefined){
  //     hashMap[s[i]] = i
  //   }else{
  //     hashMap[s[i]] = -1
  //   }
  // }
  // console.log(hashMap)
  // for(let i in hashMap){
  //   if (hashMap[i] >= 0){
  //     return hashMap[i]
  //   }
  // }
  // return -1

  // sol2 105~125ms 85~65%보다 빠름
  // n^2 
  for (let i=0; i < s.length; i++){
    var flg = 0
    for (let j=0; j < s.length; j++){
      if (i == j){ continue }
      if (s[i] === s[j]){
        flg = 1
        break
      }

    }
    if(flg == 0){
      return i
    }
  }
  return -1
  

}
console.log(firstUniqChar("abcbsa"))