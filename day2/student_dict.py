students={"ali":13,"hesam":19,"mohammad":18,"rasool":20,"khodam":16}
max_name = list(students.keys())[0]
for student in students:
    if students[student] > students[max_name]:
        max_name = student
print(max_name, students[max_name])