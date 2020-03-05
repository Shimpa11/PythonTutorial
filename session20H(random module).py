#  house no in diff sector
#
###
"""
bank account
IMEI , sim no,phone no
car number

"""


import random

#random number in range 0-10000
otp=random.randrange(10000)
print("1.otp is :",otp)

#random number in range 2000-6000 with steps of 1 by default

otp=random.randrange(2000,6000)
print("2.otp is :",otp)


#random number in range 2000-6000 with steps of 10 or multiple of 10
otp=random.randrange(2000,6000,10)
print("3.otp is :",otp)

#random number in interval 1000-9000

otp=random.randint(1000, 9000)
print("4.otp is :",otp)

# Try Implementing Algorithm for generating OTP's
# Find Algo where the same number wont be repeated