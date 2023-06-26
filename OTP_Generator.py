import os
import math
import random



digits="0123456789"
OTP=""
#Six digit password
for i in range(6):
    randomValue = math.floor(random.random()*10) 
    #print("Random Value:",randomValue)
    OTP+=digits[randomValue]
    
otp = OTP + " is your OTP"
msg= otp

print(msg)

print(range(6))

