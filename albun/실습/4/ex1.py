n = int(input())
sub = 0
stop = 666

while True:
    if '666' in str(stop):
        sub += 1
    if sub == n:
        print(stop)
        break
    stop += 1