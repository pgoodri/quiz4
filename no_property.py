class Circle:
    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius
    
    def set_radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = value

    def get_diameter(self):
        return 2 * self.get_radius()
    
    def get_area(self):
        import math
        return math.pi * self.get_radius() ** 2
    
def main():
    # Creating a circle with radius 3
    circle = Circle(3)

    # Accessing properties
    print("Radius:", circle.get_radius())
    print("Diameter:", circle.get_diameter())
    print("Area:", circle.get_area())

    # Modifying radius
    circle.set_radius(5)
    print("\nNew Radius:", circle.get_radius())
    print("New Diameter:", circle.get_diameter())
    print("New Area:", circle.get_area())

    # Trying to set negative radius (should raise an error)
    try:
        circle.set_radius(-2)
    except ValueError as e:
        print("\nError:", e)

if __name__ == "__main__":
    main()
