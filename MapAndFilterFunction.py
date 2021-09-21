# Map function
def square(x):
    return x*x

num = [1,2,3,4,5]

result = list(map(square,num))
print("Result1 :",result)


# filter function
num1 = [1,2,3,4,5]

result2 = list(filter(lambda x: x%2==0,num1))

print("Result2 :",result2)