# count = 2
# while count < 10:
#     print(f"count is: {count}")
#     count += 1
# for i in range(3):
#     for j in range(2):
  
#       print(j, end=(" "))

# print( )
# for i in range(5):
#     if i == 2:
#         continue
        
#     print(i)

# for i in range(4):
#     print(i)
# else:
#     print("loop completeed")
# count = 2
# while count < 5:
#     print(count)
#     count += 1
# else:
#     print("while loop finished")
 

# names = ["anjali", "aryal", "charlie"]
# ages = [12, 21, 56]

# for name, age in zip(names, ages):
#     print(f"{name} is {age} years old")
# countries = ["america", "Nepal", "chaina"]
# capitalcities = ["new york", "kathmandu", "beijing"]
# currencies = ["dollar", "rupees", "yuan"]

# for country, capitalcity, currency in zip(countries, capitalcities, currencies):
#     print(f"The capital of {country} is {capitalcity} and the currency is {currency}.")


# enumerate
# subjects = ["maths","science", "english"]
# marks = [56, 67, 86]

# for i, (subject, mark) in enumerate(zip(subjects, marks), start=1):
#     print(f"subject {i}: {subject} - {mark}")

# colors = ['red', 'green', 'blue']

# x, color in enumerate(colors):           //
# colors = ['red', 'green', 'blue']

# for index, color in enumerate(colors, start=1):
#     print(f"Color {index}: {color}")

#     print(f"Color {index}: {color}")

# enumerate with a list of tuple

# pairs = [("anjali", 21), ("sabita", 23), ("Charlie", 32)]

# for index, (name, age) in enumerate(pairs):
#     print(f"Person {index+1}: {name}: {age} years old")

role = "admin"
permissions = ["read", "write", "delete"]

if role == "admin":
    if "delete" in permissions:
        print("You have full access, including delete rights.")
    elif "write" in permissions:
        print("You can edit content.")
    else:
        print("You have read-only access.")
elif role == "editor":
    if "write" in permissions:
        print("You can edit content.")
    else:
        print("You have read-only access.")
else:
    print("Access denied.")

