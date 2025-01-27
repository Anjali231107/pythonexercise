# from string import Template

# template_string = "hello, ${name}! you owe $$${amount} for the ${item}s"
# t = Template(template_string)

# result = t.substitute(name="anjali", amount = 200, item= "bucket")
# print(result)

from string import Template
template_string = "return the $item to $owner."
t = Template(template_string)

d = dict(item = "box", owner = "shop")

result = t.substitute(d)
print(result)