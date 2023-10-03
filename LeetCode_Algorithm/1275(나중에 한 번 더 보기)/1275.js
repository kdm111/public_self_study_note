var tictactoe = function(moves) {
  // sol1 O(mn) O(n^2) 70~93ms 76~36%
  Board = new Array(3);
  for (let i=0; i < 3; i++){
    Board[i] = new Array(3)
  }
  for (let i=0; i < moves.length; i++) {
    i % 2 == 0 ? val = "A" : val = "B"
    let r = moves[i][0]
    let c = moves[i][1]
    Board[r][c] = val
  }
  for (let r of [0,1,2]){
    for (let c of [0,1,2]){
      ans = findWinner(r,c)
      if (ans != undefined){
        return ans
      }
    }
  }

  return moves.length == 9 ? "Draw" : "Pending"

};
function findWinner(r,c){
  chr = Board[r][c]
  dr = [0,1,0,-1, -1,1,1,-1]
  dc = [1,0,-1,0, 1,1,-1,-1]


  for(let i=0; i < 8; i++){
    var r2 = r+dr[i]; var c2 = c+dc[i]; var cnt = 1;
    while (0 <= c2 && c2 < 3 && 0 <= r2 && r2 < 3){
      if (Board[r2][c2] == undefined || Board[r2][c2] != chr){
        break
      }else{
        cnt += 1
        if (cnt == 3){
          return Board[r2][c2]
        }
      }
      r2 += dr[i]; c2 += dc[i]
    }
  }
}
console.log(tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]))

