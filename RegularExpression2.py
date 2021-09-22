import re


pattern = r"colour"
text1 = "My Favourite colour is Red. I love blue colour as we like"
text2 = re.sub(pattern, "color",text1, count=1)
print(text2)