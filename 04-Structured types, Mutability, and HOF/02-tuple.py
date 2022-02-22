t1 = (1,'two',3,6)
t2 = (t1,3.25,6)
print(t2)
sum = t1+t2
print(sum)
print((t1+t2)[3])
print((t1+t2)[2:5])

def intersect(t1,t2):
    result = ()
    for e in t1:
        if e in t2:
            result += (e,)
    return result

print('Intersection of both tuples : ',intersect(t1,t2))