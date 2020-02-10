import math

# Part 1
# Calculates the required fuel to launch the given module
def fuel_calculator(mass):
    return math.floor((mass / 3)) - 2

puzzleInput = open("input.txt", "r")
fuel_requirements = [fuel_calculator(int(mass)) for mass in puzzleInput]
modules_fuel_requirement = sum(fuel_requirements)
print(modules_fuel_requirement)

# Part 2
def fuel_of_fuel(fuel_mass):
    counter = 0
    new_fuel_requirement = fuel_calculator(fuel_mass)
    while new_fuel_requirement > 0:
        counter += new_fuel_requirement
        new_fuel_requirement = fuel_calculator(new_fuel_requirement)
    return counter

print(sum([fuel_of_fuel(x) for x in fuel_requirements]) + modules_fuel_requirement)
