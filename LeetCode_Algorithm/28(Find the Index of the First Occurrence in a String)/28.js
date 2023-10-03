var strStr = function(haystack, needle) {
  // sol2 kmp 81ms 64%
  // if (haystack.length < needle.length || needle == "") {return -1}
  // let temp = new Array(needle.length).fill(0)
  // let i = 0; let j = 1;
  // while (j < needle.length) {
  //   if (needle[i] == needle[j]) {
  //     i += 1
  //     temp[j] = i
  //     j += 1
  //   } else {
  //     if (i != 0) {
  //       i = temp[i-1]
  //     } else{
  //       temp[j] = 0
  //       j += 1
  //     }
  //   }
  // }

  // let hIdx = 0; let nIdx = 0;
  // while (hIdx < haystack.length) {
  //   if (haystack[hIdx] == needle[nIdx]) {
  //     hIdx += 1; nIdx += 1
  //   }
  //   if (nIdx == needle.length) {
  //     return hIdx-nIdx
  //   } else if (hIdx  < haystack.length && haystack[hIdx] != needle[nIdx]) {
  //     if (nIdx != 0) {
  //       nIdx = temp[nIdx-1]
  //     } else {
  //       hIdx += 1
  //     }
  //   }
  // }
  // return -1

 // sol3 56ms 68% 42.07MB 42%
  const nLength = needle.length; const hLength = haystack.length
  if (nLength > hLength || nLength == 0) {
    return -1
  }
  let kmp = new Array(nLength).fill(0)
  let i = 0; let j = 1;
  while  (j < nLength) {
    if (needle[i] == needle[j]) {
      i += 1
      kmp[j] = i
    } else {
      if (i != 0) {
        i = kmp[i-1]
        continue
      }
    }
    j += 1
  }
  console.log(kmp)
  i = 0; j = 0
  while (i < hLength && j < nLength) {
    if (haystack[i] == needle[j]) {
      i += 1; j += 1
    } else {
      if (j != 0) {
        j = kmp[j-1]
      } else {
        i += 1
      }
    }
  }
  return j == nLength ? i - nLength : -1
};


// console.log(strStr("mississippi", "issip"))
console.log(strStr("aabaaabaaac", "aabaaac"))
