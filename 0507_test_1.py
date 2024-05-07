n = int(input())
a = list(map(int, input().split()))

def duplicates(a):
    return len(a) != len(set(a))
if duplicates(a) == False:
    print("YES")
else:
    print("NO")
