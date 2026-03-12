
# Create a base class called Vehicle.

# Attributes:

# * brand
# * speed

# Method:

# * display_info() → prints the vehicle brand and speed

# Create a child class called Car that inherits from Vehicle.



class bike():
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed

    def displa_info(self):
        print("")

class retro(bike):
    pass

vehicle1=retro("yamaha",140)
print(vehicle1.brand)
print(vehicle1.speed)

