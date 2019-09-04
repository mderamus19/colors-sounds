# Define 5 of your favorite vehicles
# Move all common properties in your vehicles to a new Vehicle class.
# Create an instance of each vehicle.
# Define a different value for each vehicle's properties.
# Create a drive() method in the Vehicle class.
# Override the drive() method in all the other vehicle classes. Include the vehicle's color in the message (i.e. "The blue Ram drives past. RRrrrrrummbbble!").
# Create a turn(self, direction) method, and a stop(self) method on Vehicle. Define a basic implementation of each.
# Override all three of those methods on some of the vehicles. For example, the stop() method for a plane would be to output the message "The white Cessna rolls to a stop after rolling a mile down the runway."
# Make your vehicle instances perform all three behaviors.
class Vehicle:
    '''common properties of the vehicle'''
    def __init__(self, color, maximum_occupancy):
        '''initialize vehicle attributes'''
        self.color = color
        self.maximum_occupancy = maximum_occupancy

    def drive(self, drive):
        '''method to drive the vehicle'''
        self.drive = ""
        print(f"I drive {drive}")

    def turn(self, direction):
        '''method to turn the vehicle'''
        self.direction = ""
        print(f"I turn to the {direction}")

    def stop(self):
        '''method to stop the vehicle'''
        self.stop = ""
        print("I stop quickly")

class Boat(Vehicle):
    '''create a replica of a boat'''
    def __init__(self, sail):
        self.sail = sail

    def drive(self):
        '''method to override vehicle drive method'''
        print("I drive my color boat fast!!")

    def stop(self):
        '''method to override vehicle stop method'''
        print("Sometimes I stop the boat to float!")

class Plane(Vehicle):
    def __init__(self, engine):
        self.engine = ''

    def drive(self, drive):
        print("I don't drive my purple plane.")

    def stop(self):
        print("The purple plane stops quickly on the runway.Errrrrrr!!!!")

class Train(Vehicle):
    def __init__(self, locomotive):
        self.locomotive = ''

    def drive(self, drive):
        print("I drive my blue train fast!")

    def turn(self):
        '''method to override vehicle turn method'''
        print("If I turn the train, I will go off the track.")

class Car(Vehicle):
    def __init__(self, wheels):
        self.wheels = ''

    def drive(self, drive):
        print("I drive my black car fast..VROOOMMMMM!")

    def turn(self,direction):
        print("The red car turned left at the light.")

class Motorcycle(Vehicle):
    def __init__(self, wheels):
        self.wheels = ''

    def drive(self):
        print("I drive fast and furious on my motorcycle!")

yacht = Boat("swift")
yacht.drive()
yacht.turn("left")
yacht.stop()
yacht.color="blue"
yacht.maximum_occupancy = 4
boeing757 = Plane("engine")
boeing757.drive("fast")
boeing757.turn("left")
boeing757.stop()
thomas = Train("locomotive")
thomas.drive("slow")
thomas.turn()
thomas.stop()
maxima = Car(4)
maxima.drive("smooth")
maxima.turn("right hard")
maxima.stop()
harley = Motorcycle(2)
harley.drive()
harley.turn("carefully")
harley.stop()
