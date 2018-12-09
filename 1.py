ans = 0
for i in range(1,1001):
    if (i%2 == 0) and (i%3==0 or i%5==0):
        ans += 1
print(ans)
