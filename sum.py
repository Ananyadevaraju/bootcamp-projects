# e=[]
# while True:
# 	n=(input())
# 	if n=="end":
# 		break
#     e.append(int(n)) 
# for i in e:
# 	sum += i
# print(sum)

# e = [1,2,3,4]
e = input("Enter numbers: ")
a = e.split()
b = []
for i in a:
	b.append(int(i))
# x = map(int, e.split())
a = 0
for i in b:
	a +=i
print(a)
