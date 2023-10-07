# greedy

def solution(cap, n, deliveries, pickups):
    ans = 0; de = 0; pi = 0;
    for i in range(n-1, -1, -1):
        de += deliveries[i]; pi += pickups[i]
        if de > 0 or pi > 0:
            val = max(de, pi) // cap 
            if max(de, pi) % cap:
                val += 1
            ans += 2 * (i + 1) * val
            de -= cap * val; pi -= cap * val
    return ans
    
        

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
print(solution(2, 2, [0,0], [0, 4]))
print(solution(2, 2, [1,0], [1, 0]))
print(solution(4, 4, [0,0,25, 24, 51, 0], [0,0,51, 0, 0, 49] ))



