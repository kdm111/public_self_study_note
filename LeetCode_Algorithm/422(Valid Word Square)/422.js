var validWordSquare = function(words) {
  for(let i=0; i < words.length; i++){
    let w = words[i], rev = ''
    for(let j=0; r < words.length; j++){
      rev += (words[j][i] || '')
    }
    if(rev !== w) return false
  }
  return true
};