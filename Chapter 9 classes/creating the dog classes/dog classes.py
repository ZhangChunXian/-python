class Dog(object):
    # a simple attempt to model a dog

    def _init(self,name,age):
        # initialize name and age attributes.
        self.name = name
        self.age = age

    def sit(self):
        # simulate a dog sitting in response to a command
        print(self.name.title()+"is now sitting.")

    def roll_over(self):
        # simulate rolling over in response to a command.
        print(self.name.title()+"rolled over!")

        pass
        