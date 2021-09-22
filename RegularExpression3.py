# Meta characters  65 no
import re

pattern = r"colo.r"

if re.match(pattern, "colour"):
    print("Matched")