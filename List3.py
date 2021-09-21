
n = input("Enter a text of number")
#10 20 30

list = n.split() #20, 20, 40, 30
sum = 0

for num in list:
    sum = sum + int(num)

print(sum)
