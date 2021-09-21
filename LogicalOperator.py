# Logical Operator use and/or

# 3 number in print big number
num1 = 20
num2 = 110
num3 = 40

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3)

# vowel - a,e,i,o,u
ch= 't'

if ch == 'a' or ch =='e' or ch == 'i' or ch == 'o' or ch == 'u':
    print("Vowel")
else:
    print("Consonant")