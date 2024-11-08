#our Cat Entity
class Cat:
    #the constructor
    # - the constructor will create a cat for us in code 
    # - to create a cat, we need given_name & given_colour
    def __init__(self, given_name, given_colour):
        self.name = given_name
        self.colour = given_colour

# an instance of Cat
# an instance is a specific occurrence of a class
mimi = Cat("Mimi","Brown")
print(mimi.name)
print(mimi.colour)