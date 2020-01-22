students=["jack","Joe","Tom","Fiona"]
print(students,hex(id(students)))

 # concatenation
newStudents=students+["jane"]
# newStudents=students+["jane"]

print(newStudents, hex(id(newStudents)))
# memory leak

students=students+["jane"]
print(students ,hex(id(students)))

someStudents=["Jim","joe"]
print(someStudents in newStudents)
