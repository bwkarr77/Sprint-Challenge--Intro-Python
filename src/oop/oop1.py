# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle:
    def __init__(self, var_v):
        self.var_v = var_v

    def __str__(self):
        return f'variable: {self.var_v}'


class FlightVehicle(Vehicle):
    def __init__(self, var_f, var_v):
        self.var_f = var_f
        super().__init__(var_v)
        # Vehicle is base class, var_v is from Vehicle class

    def __str__(self):
        return f'var_f: {self.var_f}, var_v: {self.var_v}'


class Starship(FlightVehicle):
    # FlightVehicle is the base/parent class
    pass


class Airplane(FlightVehicle):
    # FlightVehicle is the base/parent class
    pass


class GroundVehicle(Vehicle):
    def __init__(self, var_g, var_v):
        self.var_g = var_g
        super().__init__(var_v)
        # Vehicle is base class, var_v is from Vehicle class

    def __str__(self):
        return f'var_v: {self.var_v}, var_g: {self.var_g}'


class Car(GroundVehicle):
    # GroundVehicle is the base/parent class
    pass


class Motorcycle(GroundVehicle):
    # GroundVehicle is the base/parent class
    pass

