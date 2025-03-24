n = int(input())
tmp = ''
if n % 2:
    for _ in range(n // 2):
        tmp += '-'
    ans = tmp + '=' + tmp
else:
    for _ in range(n // 2 - 1):
        tmp += '-'
    ans = tmp + '==' + tmp
print(ans)
