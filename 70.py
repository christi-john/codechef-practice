# FRK

check=['ch','he','ef','che','chef','hef']
count=0
for _ in range(int(input())):
    friend=input()
    for i in check:
        if i in friend:
            count+=1
            break
print(count)