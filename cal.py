# a = 50
# b = 3

# print("The value of" , a, "+", 3, "is: ", a + b)
# print("The value of" , a, "-", 3, "is: ", a - b)
# print("The value of" , a, "*", 3, "is: ", a * b)
# print("The value of" , a, "/", 3, "is: ", a / b)

score = int(input("Score: "))

if 90<= score and score <= 100:
    print("Grade: A")
elif 80<= score and score <= 90:
    print("Grade: B")
elif 70<= score and score <= 80:
    print("grade: C")
elif 80<= score and score <= 70:
    print("Grade: D")
else:
    print("Grade: F")