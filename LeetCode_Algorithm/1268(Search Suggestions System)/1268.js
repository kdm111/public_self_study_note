var suggestedProducts = function(products, searchWord) {
  // sol1 86ms 93% 54.7MB 45%
  products = products.sort((a,b) => {
    return (b > a) ? -1 : 1
  })
  let start = 0; let end = products.length-1
  let ans = []
  for (let [i,c] of Object.entries(searchWord)){
    while (start <= end && (i >= products[start].length || c > products[start][i])) {
      start += 1
    }
    while (start <= end && (i >= products[end].length || c < products[end][i])) {
      end -= 1
    }
    if (start <= end) {
      ans.push(products.slice(start, Math.min(start+3, end+1)))
    } else {
      ans.push([])
    }
  }
  return ans
};

console.log(suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse"))