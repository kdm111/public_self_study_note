var numUniqueEmails = function(emails) {
  // sol1 147ms 26% 498MB 11%
  data = new Set()
  for (let email of emails) {
    let name = findName(email)
    let mail = findEmail(email)
    let person = name.concat('@').concat(mail)
    data.add(person)
  }
  return data.size
};
var findName = function(email) {
  ret = ""
  for (let c of email) {
    if (c == '.') {
      continue
    } else if (c == '+' || c == '@') {
      break ;
    } else {
      ret += c
    }
  }
  return ret
}
var findEmail = (email) => {
  let ret = ""; let i = email.length-1
  while (email[i] != '@') {
    ret += email[i]
    i -= 1
  }
  return ret.split("").reverse().join("")
}