ans = int(input())

if ans>100:
    print("NO")
elif ans<1:
    print("NO")
elif ans % 2 == 0 and ans != 2:
    print("YES")
else:
    print("NO")