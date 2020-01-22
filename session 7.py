# students=["jack","Joe","Tom","Fiona"]

#
#sets operations. set is unordered due to hashing. data will be unique. eg email id

students={"jack","Joe","Tom","tom","Fiona"}
print(students,hex(id(students)))

# no concatenationation on sets
# newStudents=students+{"Jin","Jane"}
# print(newStudents, hex(id(newStudents)))

# newStudents=students+["Jin","Jane"]
# # print(newStudents, hex(id(newStudents)))
#
# newStudents=students+("Jin","Jane")
# print(newStudents, hex(id(newStudents)))
# no indexing and slicing no repetition no basic For loop

# newSet=set*2
# print(newSet)
for student in students:
    print(student)



# membership test
print("Jam" in students)
print("Tom" in students)