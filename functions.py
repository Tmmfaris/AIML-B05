# functions.py

# FUNCTION 1: Calculate total marks
def calculate_total(marks):
    return sum(marks.values())


# FUNCTION 2: Calculate average marks
def calculate_average(marks):
    total = calculate_total(marks)
    return round(total / len(marks), 2)


# FUNCTION 3: Assign grade based on average marks
def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


# FUNCTION 4: Check pass/fail
def check_result(marks, pass_mark=40):
    for mark in marks.values():
        if mark < pass_mark:
            return "Fail"

    return "Pass"


# FUNCTION 5: Create a summary for one student
def student_summary(student):
    marks = student["marks"]
    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = get_grade(average)
    result = check_result(marks)

    return {
        "name": student["name"],
        "total": total,
        "average": average,
        "grade": grade,
        "result": result
    }


# FUNCTION 6: add a new student
def add_student(data, student_id, name, **marks):
    if student_id in data:
        return False
    
    data[student_id] = {"name": name, "marks": dict(marks)}
    return True


# FUNCTION 7: Update marks for an existing student
def update_marks(data, student_id, **changes):
    if student_id not in data:
        return False
    
    data[student_id]["marks"].update(changes)
    return True


# FUNCTION 8: Remove a student
def remove_student(data, student_id):
    if student_id not in data:
        return False

    data.pop(student_id)
    return True


# FUNCTION 9: Print class report
def print_report(data):
    print(f"{'ID':<6}{'Name':<8}{'Total':>6}{'Avg':>8}{'Grade':>7} Result")

    print("-" * 42)

    ranking = []

    for student_id, student in data.items():
        average = calculate_average(student["marks"])
        ranking.append((average, student_id))

    ranking.sort(reverse=True)

    for average, student_id in ranking:
        student = data[student_id]
        summary = student_summary(student)

        print(f"{student_id:<6}{summary['name']:<8}{summary['total']:>6}{summary['average']:>8}{summary['grade']:>7} {summary['result']}")


# FUNCTION 10: Calculate class statistics
def class_statistics(data, *subjects):
    if not data:
        return {
            "topper": None,
            "pass_percentage": 0.0,
            "subject_averages": {}
        }

    topper_id = max(
        data,
        key=lambda sid: calculate_average(data[sid]["marks"])
    )

    topper_name = data[topper_id]["name"]

    passed_count = 0

    for student in data.values():
        if check_result(student["marks"]) == "Pass":
            passed_count += 1

    pass_percentage = round(
        passed_count / len(data) * 100, 1
    )

    subject_averages = {}

    for student in data.values():
        for subject, mark in student["marks"].items():
            if not subjects or subject in subjects:
                subject_averages.setdefault(subject, [])
                subject_averages[subject].append(mark)

    for subject, marks in subject_averages.items():
        subject_averages[subject] = round(
            sum(marks) / len(marks), 1
        )

    return {
        "topper": topper_name,
        "pass_percentage": pass_percentage,
        "subject_averages": subject_averages
    }




