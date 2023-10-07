class DSU:
    def __init__(self):
        self.par = [i for i in range(2501)]
        self.rnk = [None for _ in range(2501)]

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        return True

class COMMAND:
    def __init__(self, command, dsu):
        self.comm = command.split(" ")
        if self.comm[0] == "UPDATE":
            if len(self.comm) == 4:
                r, c, v = self.comm[1], self.comm[2], self.comm[3]
                self.UPDATE(r, c, v, dsu)
            if len(self.comm) == 3:
                old, new = self.comm[1], self.comm[2]
                self.REPLACE(old, new, dsu)
        elif self.comm[0] == "MERGE":
            pass
        elif self.comm[0] == "UNMERGE":
            pass
        elif self.comm[0] == "PRINT":
            r, c = self.comm[1], self.comm[2]
            return self.PRINT(r, c, dsu)


    def UPDATE(self, r, c, v, dsu):
        i = 50 * (r-1) + c
        dsu[i] = v

    def REPLACE(self, old, new, dsu):
        for i in range(len(dsu)):
            if dsu[i] == old:
                dsu[i] = new

    def MERGE(self):
        
        pass
    def UNMERGE(self):
        pass
    def PRINT(self, r, c, dsu):
        if dsu[50 * (r - 1) + c] != None:
            return dsu[50 * (r - 1) + c]
        else:
            return "EMPTY"

def solution(commands):
    answer = []
    dsu = DSU()
    for command in commands:
        val = COMMAND(command, dsu)
        if val != None:
            answer.append(val)
    return answer
print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))