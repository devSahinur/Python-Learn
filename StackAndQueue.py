from collections import deque
# Stack
books = []
books.append("C")
books.append("Python")
books.append("JavaScript")
print(books)

books.pop()
print("Now the top book is ",books[-1])

books.pop()
print("Now the top book is ",books[-1])

books.pop()
if not books:
    print("No books left")

# Queue


bank = deque(["Sahinur","karim","Karemul"])
bank.popleft()
print(bank)

if not bank:
    print("NO person left")