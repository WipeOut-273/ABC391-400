n, m = map(int, input().split())
A = list(map(int, input().split()))
B = []
for num in range(1, n + 1):
    if num not in A:
        B.append(num)
print(len(B))
print(*B)
