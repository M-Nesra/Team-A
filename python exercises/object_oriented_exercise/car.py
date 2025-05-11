from math import radians,sin,cos

class Car:
    """
    Represents a car that can move and turn.

    Attributes:
        x (float): The car's x-coordinate.
        y (float): The car's y-coordinate.
        heading (float): The direction the car is facing, in degrees.
    """
    
    def __init__(self, x=0.0, y=0.0, heading=0.0):
        """
        Initializes the car with a starting position and direction.

        Args:
            x (float, optional): Starting x-coordinate. Default is 0.
            y (float, optional): Starting y-coordinate. Default is 0.
            heading (float, optional): Starting direction in degrees. Default is 0.
        """
        self.x = x
        self.y = y
        self.heading = heading
    
    def turn(self, degrees):
        """
        Turns the car by a given number of degrees.

        Args:
            degrees (float): How much to turn (positive for right, negative for left).
        """
        self.heading = (self.heading + degrees) % 360
    
    def drive(self, distance):
        """
        Moves the car forward in the direction it is facing.

        Args:
            distance (float): How far to move.
        """
        h = radians(self.heading)
        self.x += distance * sin(h)
        self.y -= distance * cos(h)

def sanity_check():
    """
    Tests the Car class by making it move and turn.
    """
    car = Car()
    car.turn(90)
    car.drive(10)
    car.turn(30)
    car.drive(20)
    print(f"Location: {car.x}, {car.y}")
    print(f"Heading: {car.heading}")
    return car

if __name__ == "__main__":
    sanity_check()
