bracketMap = {
  "(" : ")",
  "{" : "}",
  "[" : "]"
}

var isValid = function(s) {
  // 104ms or 56ms 38%보다 빠름 or 98%보다 빠름 
  var stack = []
  for (let bracket of s){
    if (bracket in bracketMap){
      stack.push(bracket)
    }
    else{
      if (!stack) {return false}
      else{
        const stackBracket = stack.pop()
        if (bracketMap[stackBracket] == bracket){continue}
        else {return false}
      }
    }
  }

  if (stack.length){return false}
  else {return true}  
};
console.log(isValid("}"))