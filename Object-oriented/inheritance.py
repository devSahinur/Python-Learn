# inheritance is one class attrebute others class copy
class Phone:
    def call(self):
        print("You can call")
    
    def message(self):
        print("You can message")

class Samsung(Phone):
    # call, message
    def photo(self):
        print("You can take photo")

p = Phone()
p.message()
p.call()

s = Samsung()
s.message()
s.call()
s.photo()


# check
print(issubclass(Samsung, Phone))