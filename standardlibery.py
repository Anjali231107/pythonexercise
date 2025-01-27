# from datetime import date
# now = date.today()
# print(now)

# now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")


# # dates support calendar arithmetic
# birthday = date(1964, 7, 31)
# age = now - birthday
# age.days
# print(age)

# import sys
# print(sys.argv)
# import os
# dir(os)
# help(os)

# using math in standardlibrary
# import math
# result = math.sqrt(16)
# print(result)


# using datetime

# from datetime import datetime
# now = datetime.now()
# print(now)
# String Pattern Matching
# from urllib.request import urlopen
# with urlopen('https://www.example.com') as response:
#     html = response.read()
#     print(html)



# import smtplib
# server = smtplib.SMTP('localhost')
# server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
# """To: jcaesar@example.org
# From: soothsayer@example.org

# Beware the Ides of March.
# """)
# server.quit()
from datetime import date
now = date.today()
print("today is", now)