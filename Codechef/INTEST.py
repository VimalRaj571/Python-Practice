#INTEST
loop, div = map(int, input().split())
count=0
while loop>0:
    inp = int(input())
    if inp%div ==0:
        count+=1
    loop=loop-1
print(count)