def letter(score):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    if (score % 10 >= 7) and (grade not in["A","F"]):
        grade += "+"
    elif (score % 10 <= 3) and (grade != "F"):
        grade += "-"
    return grade
            
   