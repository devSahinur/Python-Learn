#xargs
def student(*details):
    print(details)

student(101,"Sahinur Islam",3.68)

# xxargs
def students(**details):
    print(details)

students(id=111, name="Sahinur")