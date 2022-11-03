def fi(n):
    if n==1 or n==2:
        return 1
    return fi(n-1)+fi(n-2)

print(fi(4))

def btup(n):
    d = [0]*(n+1)
    d[1] = 1
    d[2] = 1
    for i in range(3, n+1):
        d[i] = d[i-1] + d[i-2]

    return d[n]

print(btup(4))