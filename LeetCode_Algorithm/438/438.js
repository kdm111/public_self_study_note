function isEqual(s_list, p_list) {
  for (let idx in s_list){
    if (s_list[idx] != p_list[idx]) {
      return false
    }
  }
  return true
}

var findAnagrams = function(s, p) {
  
  // sol4 O(n^2) 165ms 55%
  if (s.length < p.length) {return []}
  sList = new Array(26).fill(0)
  pList = new Array(26).fill(0)
  for (let idx=0 ; idx < p.length; idx++) {
    sList[s[idx].charCodeAt(0) - 97] += 1
  }
  for (let c of p) {
    pList[c.charCodeAt(0) - 97] += 1
  }

  ans = []
  if (isEqual(sList, pList) == true){
    ans.push(0)
  }

  for (let idx=0; idx < s.length-p.length; idx++){
    sList[s[idx].charCodeAt(0) - 97] -= 1
    sList[s[idx + p.length].charCodeAt(0) - 97] += 1
    console.log(sList)
    // if (isEqual(sList, pList) == true) {
    //   ans.push(idx+1)
    // }

    // sol5 toString() equal sign 497ms 
    // 
    if (sList.toString() == pList.toString()){
      ans.push(idx+1)
    }
  }
  return ans
  
};
// console.log(findAnagrams("abab", "ab"))
console.log(findAnagrams("cbaebabacd", "abc"))
