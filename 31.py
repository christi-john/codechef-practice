# AREAPERI

L=int(input())
B=int(input())
area=L*B
peri=2*(L+B)
if area>peri:
    print("Area")
    print(area)
elif peri>area:
    print("Peri")
    print(peri)
else:
    print("Eq")
    print(area)