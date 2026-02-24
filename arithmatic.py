print(30+12)
print(30-12)
print(30*12)
print(30/12)
print(30//12)
print(30%12)
c=10**2
print(c)
print("the value of c is {}".format(c))
print(f"the value of c is {c}")
print("%d" % c)

print(10==10)
print(10!=10)
print(10>5)     
print(10<5)
print(10>=10)
print(10<=10)

x=5
print(x<5 and x>0)
print(x<5 or x>0)
print(not(x<5 and x>0))
print(12 and 13)
print(0 and 13)
print(12 or 13)

a=2 #00000010
b=3 #00000011
print(a&b) #2
print(a|b) #3
print(~a) #-3
print(a^b) #1
print(a<<2) #8
print(a>>2) #0

a=10
b=a
print(a is b) #True
l1=[10,20,30]
l2=[10,20,30]
print(l1 is not l2) #True


if 100 not in (10,20,20,40):
    print("correct")
else:
    print("incorrect")    
