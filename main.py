import math


# Calculates the required fuel to launch the given module
def fuel_calculator(mass):
    return math.floor((mass / 3)) - 2


puzzleInput = open("input.txt", "r")
fuel_requirements = [fuel_calculator(int(mass)) for mass in puzzleInput]
modules_fuel_requirement = sum(fuel_requirements)
print(modules_fuel_requirement)

total_fuel_counter = 33583
new_fuel_requirement = fuel_calculator(33583)
#total_fuel_counter += new_fuel_requirement

while new_fuel_requirement > 1:
    print("fuel for fuel " + str(new_fuel_requirement))
    total_fuel_counter += new_fuel_requirement
    new_fuel_requirement = fuel_calculator(new_fuel_requirement)
    #total_fuel_counter += new_fuel_requirement

print(total_fuel_counter)