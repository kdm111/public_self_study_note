var reverseVowels = function(s) {
  // sol2 129ms 62%
  let arr = Array.from(s)
  let left = 0
  let right = s.length-1
  const vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
  while (left < right) {
    while (left < s.length && vowels.indexOf(arr[left]) < 0) {
      left += 1
    }
    while (right >= 0 && vowels.indexOf(arr[right]) < 0) {
      right -= 1
    }
    if (left >= right) {
      break ;
    }
    [arr[left], arr[right]] = [arr[right], arr[left]]
    left += 1
    right -= 1    
  }
  return arr.join('')
};

console.log(reverseVowels("hello"))