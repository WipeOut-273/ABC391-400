n = int(input())
L = list(map(int, input().split()))

ans = 'No'
for i in range(n - 2):
    if L[i] == L[i + 1] == L[i + 2]:
        ans = 'Yes'
print(ans)
