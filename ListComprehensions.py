# {expression for item in list} (map)
num = [1,2,3,4,5]

result = [x*x for x in num]

print("Result :",result)

# {expression for item in list} (filter)
num1 = [1,2,3,4,5]

result2 = [x for x in num1 if x%2==0]


print("Result2 :",result2)