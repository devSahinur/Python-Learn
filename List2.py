# List Lenths

subjects = ["C", "C++", "Java", "Python", "JavaScript"]
print(len(subjects))

# List append

subjects.append("JavaScrip Lover")
print(subjects)

# List insert
subjects.insert(2,"Go")
print(subjects)

# List item remove 
subjects.remove("Python")
print(subjects)

# List sorting 
subjects.sort()
print(subjects)

# List Reverse
subjects.reverse()
print(subjects)

# List pop 
subjects.pop()
print(subjects)

# List clear
# subjects.clear()
# print(subjects)

# List copy
# subjects2 = subjects.copy()
# print(subjects2)

# List one items position
pos = subjects.index("Go")
print(pos)

# List count function
count = subjects.count("Go")
print(count)