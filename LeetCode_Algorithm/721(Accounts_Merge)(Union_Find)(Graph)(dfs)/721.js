var accountsMerge = function(accounts) {
  // sol1 3711ms 5%
  let emailOfName = new Map();
  let emailGraph = new Map();

  for (let account of accounts) {
    let name = account[0]
    for (let email of account.slice(1, )) {
      if (emailGraph[account[1]] == undefined) {
        emailGraph[account[1]] = new Set([email])
      } else {
        emailGraph[account[1]].add(email)
      }
      if (emailGraph[email] == undefined) {
        emailGraph[email] = new Set([account[1]])
      } else {
        emailGraph[email].add(account[1])
      }
      emailOfName[email] = name
    }
  }
  let ans = []; let visited = []
  for (let email in emailGraph) {
    let name = [emailOfName[email]]
    if (visited.indexOf(email) < 0) {
      visited.push(email)
      let temp = [email]; let emails = []
      while (temp.length > 0) {
        let e = temp.pop()
        emails.push(e)
        for (let em of emailGraph[e]) {
          if (visited.indexOf(em) < 0) {
            visited.push(em)
            temp.push(em)
          }
        }
      }
      let t = name.concat(emails.sort())
      ans.push(t)
    }
  }
  return ans
};

console.log(accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))