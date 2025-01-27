# if statement

# x = int(input("Please enter an integer"))
# if x<2:
#     x = 0
#     print("negative change to Zero")
# elif x==0:
#     print("zero")
# elif x==1:
#     print("single")
# else:
#     print("more")




# for statement
# name = ["anjali", "prasad", "aryal"]
# for x in name:
#     print(x, len(x))

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

#  Iterate over a copy
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]

# Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status
     
    #  4.4. break and continue Statements

    for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break