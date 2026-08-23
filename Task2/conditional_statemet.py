student=int(input("enter the marks:"))
if student>=90 and student<=100:
    print("gardes:A+")
elif student>=80 and student<=89:
    print("grades:A")
elif student>=70 and student<=79:
    print("grades:B")
elif student>=60 and student<=69:
    print("grades:c")
elif student>=50 and student<=59:
    print("grades:D") 
elif student<50:
    print("Fail")
else:
    print("invalid")
