#l=[1,2,3,4,5]
#mul=1
#for i in l:
#	mul *= i
#print(mul)

e=input("enter the numbers: ")
a=e.split()
b=[]
for i in a:
	b.append(int(i))

mul=1
for i in b:
	mul *= i
print(mul)
