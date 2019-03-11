student_marks = {}
n = int(input("Enter number of students: "))
for i in range(n):
	name,*line = input("Enter name and subject marks in the same line: ").split()
	scores = list(map(int,line))
	student_marks[name] = scores 
print(student_marks)

query_name , query_subject = input("Enter student name and the subject: ").split()
l = student_marks[query_name]
print(l)
subjects = {0:"math",1:"physics",2:"chemistry",3:"biology",4:"social-sciences"}

for key,value in subjects.items():
	if query_subject.lower() == value:
		print(f"{query_name} has scored {l[key]} in {query_subject}")

query_subject = input("Enter the subject: ")
for key,value in subjects.items():
	if query_subject.lower() == value:
		index = key 
a=[]
for name,score in student_marks.items():
	print(name,score[index])
	a.append([name,score[index]])
print(a)

	