scores={"ali":13,"hesam":19,"mohammad":18,"rasool":20,"khodam":16}
max_student = "ali"
for student, score in scores.items():
    if score > scores[max_student]:
        max_student = student
print(max_student, scores[max_student])