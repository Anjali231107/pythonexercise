# url = input("URL: ").strip()

# username = url.replace("https://twitter.com/", "")
# print(f"Username: {username}")



# num = [1,2,3,4,5,6,7,8,9,"apple","ball","cat"]
# stringa = [ ]
# print(num[0])
# for x in string:
#     print(x)

# for s in num:
#     if isinstance (s,str):
#         stringa.append (s)

# print(stringa[0])

# for(int i=0;i>=10;i++){

# }
# 

# for i in range(3):
#  print(f"{i+1}")
#  for j in range(1, 4):
#   print (j, end = "\n ")

# print()

# for _ in range(3):
#  print("1 2 3")
for i in [1,2,3]:  # Outer loop (one iteration, just for nesting)
    for j in [1,2,3,4,]:  # Inner loop to print 123 four times
        print(j, end=" ")
    print()