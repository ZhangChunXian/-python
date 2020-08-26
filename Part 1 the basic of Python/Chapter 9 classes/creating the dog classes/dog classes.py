class Dog:
    # 2.A simple attempt to model a dog.
    
    # 3.
    def __init__(self,name,age):
        # Initialize name and age attributes.
    # 4.
        self.name=name
        self.age=age

    # 5.
    def sit(self):
        # Simulate a dog sitting in response to a command.
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        #Simulate rolling over in response to a command.
        print(f"{self.name} rolled over!")

# Making a instance from a class
    #1
    my_dog = Dog("Willie",6)
    #2
    print(f"My dog's name is {my_dog.name}.")
    #3
    print(f"My dog is {my_dog.age} years old.")

    alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
    print(f"Orignial position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
     x_increment = 3
    
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")
alien_0['speed'] = 'fast'

favorite_lanuages = {'jen': Python, 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
lanuages = favorite_lanuages['sarah'].title()
print(f"{lanuages}")

