S = list(input())
T = 0

piano = {"d":0, "r":1, "m":2, "f":3, "s":4, "l":5, "c":6}

u = "m"

for i in range(len(S)):
    T += 1
    T += abs(piano[u]-piano[S[i]])
    u = S[i]

print(T)
