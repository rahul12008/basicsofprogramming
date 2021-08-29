import math as m
#question : to check below points are vertices of square or not
p1=(0,1)
p2=(1,4)
p3=(4,3)
p4=(3,0)
set1=set()
set1.add(m.dist(p1,p2))
set1.add(m.dist(p1,p3))
set1.add(m.dist(p1,p4))
set1.add(m.dist(p2,p3))
set1.add(m.dist(p2,p4))
set1.add(m.dist(p3,p4))
print(set1)
if len(set1)==2:  #checking if all sides are equal and diagonals are equal
    a=set1.pop()
    b=set1.pop()
    if a>b:
        if a==m.sqrt(2)*b:   #checking diagonal condition
            print("it is square")
    else:
        if b==m.sqrt(2)*a:   #checking diagonal condition
            print("it is square")
else:
    print('not square')
        


