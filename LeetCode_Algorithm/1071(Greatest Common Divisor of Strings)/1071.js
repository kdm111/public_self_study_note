var gcdOfStrings = function(str1, str2) {
  // sol1 93ms 67% 42.1MB 89%
  if (str1.length < str2.length) {
    let temp = str1;
    str1 = str2;
    str2 = temp
  }  
  if (str1.slice(0, str2.length) == str2) {
    if (str1 == str2) {
      return str2
    }
    return gcdOfStrings(str2, str1.slice(str2.length, ))
  }
  return ""
};