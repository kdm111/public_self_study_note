var isIsomorphic = function(s, t) {
  // 121ms 32%
    s_t = {}
    t_s = {}

    for (let idx = 0; idx < s.length; idx ++ ){
      if (s_t[s[idx]] == undefined) {
        s_t[s[idx]] = t[idx]
      } else {
        if (s_t[s[idx]] != t[idx]){
          return false
        }
      }
      if (t_s[t[idx]] == undefined) {
        t_s[t[idx]] = s[idx]
      } else {
        if (t_s[t[idx]] != s[idx]){
          return false
        }
      }
    }
    return true
};

console.log(isIsomorphic("foo", "baa"))
console.log(isIsomorphic("baba", "badc"))
