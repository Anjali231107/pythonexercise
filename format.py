import re

name = input("what's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}"
    
print(f"hello, {name}")

#     last, first = matches.groups()
#     name = f"{first} {last}"
# print(f"hello, {name}")
# if "," in name:
#     last, first = name.split("")
#     name = f"{first} {last}"
# print(f"hello, {name}")