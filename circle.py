class Circle:
    _pi = 3.14
    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2
    def calculate_circumference(self, diameter):
        return Circle._pi * diameter
    def calculate_area(self, radius):
        return Circle._pi * (radius ** 2)
    def calculate_area_of_sector(self, angle, radius):
        return (angle / 360) * Circle._pi * (radius ** 2)
circle = Circle(10)
angle = 5
diameter = 6
radius = diameter / 2
print(f"{circle.calculate_circumference(diameter):.2f}")
print(f"{circle.calculate_area(radius):.2f}")
print(f"{circle.calculate_area_of_sector(angle, radius):.2f}")
