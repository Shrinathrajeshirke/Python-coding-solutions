# > **Write a program that:**
# > - Creates a dictionary of a student's subjects and marks
# > - Finds total, average, highest and lowest scoring subject
# > - Prints pass/fail (passing marks = 40)

def marks_evaluation():
    subjects = {
    "Maths": 85,
    "Science": 42,
    "English": 78,
    "History": 35,
    "Python": 95
    }
    count_pass = 0
    count_fail = 0
    for subject, marks in subjects.items():
        if marks >= 40:
            status = "pass"
            count_pass += 1 
        else: 
            status = "fail"
            count_fail += 1
        print(f"{subject} -> {marks} -> {status}")
        
    total_marks = sum(subjects.values())
    average_marks = total_marks/len(subjects)
    Highest_marks = max(subjects.values())
    lowest_marks = min(subjects.values())
    
    if count_pass > count_fail:
        Result = "PASS"
    else:
        Result = "FAIL"
    
    print(f"Total marks: {total_marks}")
    print(f"Average marks: {average_marks}")
    print(f"Highest marks: {" ".join([k for k,v in subjects.items() if v==Highest_marks])}")
    print(f"Lowest marks: {" ".join([k for k,v in subjects.items() if v==lowest_marks])}")
    print(f"Result: {Result}")

marks_evaluation()