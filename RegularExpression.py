import re
# match function
pattern = r"colour"
if re.match(pattern,"colour Red is a colour, I Love red colour"):
    print("Match")

else:
    print("Not Matched")

# search function
pattern = r"colour"
if re.search(pattern,"Red is a colour, I Love red colour"):
    print("Match")

else:
    print("Not Matched")

# findall function
pattern = r"colour"
print(re.findall(pattern,"Red is a colour, I Love red colour"))


#  again search function
pattern = r"colour"
text = "My favorite colour is Blue"
match = re.search(pattern,text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())