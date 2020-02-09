import math


# Calculates the required fuel to launch the given module
def fuel_calculator(mass):
    return math.floor((mass / 3)) - 2


puzzleInput = open("input.txt", "r")
fuel_requirements = [fuel_calculator(int(mass)) for mass in puzzleInput]
total_fuel_requirement = sum(fuel_requirements)
print(total_fuel_requirement)