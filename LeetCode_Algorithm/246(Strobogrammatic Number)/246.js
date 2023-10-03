var isStrobogrammatic = function(num) {
  // sol1 91ms 49% 42.5MB 5%
  // O(n) O(1)
  hashMap = {
  '0' : '0', 
  '1' : '1',
  '5' : '2',
  '6' : '9',
  '8' : '8',
  '9' : '6'
  }
  for (let i = 0; i < parseInt(num.length/2)+1; i++) {
    if (hashMap[num[i]] == undefined) {
      return false
    }
    let left = num[i]; let right = num[num.length-1-i]
    if (hashMap[left] != right) {
      return false
    } 
  }
  return true
};
console.log(isStrobogrammatic("2"))