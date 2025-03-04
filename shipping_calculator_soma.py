# Package Express Shipping Rate Calculator
# Created by: Sarah Johnson
# Last modified: March 2024

# Initialize the program with a welcome message
print("Welcome to Package Express. Please follow the instructions below.")

# Request and validate package weight
item_weight = float(input("Please enter the package weight:\n"))

# Weight validation check
if item_weight > 50:
    print("Package too heavy to be shipped via Package Express. Have a good day.")
    exit()

# Collect package measurements
box_width = float(input("Please enter the package width:\n"))
box_height = float(input("Please enter the package height:\n"))
box_length = float(input("Please enter the package length:\n"))

# Sum up all dimensions
dimension_sum = box_width + box_height + box_length

# Size validation check
if dimension_sum > 50:
    print("Package too big to be shipped via Package Express.")
    exit()

# Compute shipping cost using the formula
# Cost = (width * height * length * weight) / 100
delivery_cost = (box_width * box_height * box_length * item_weight) / 100

# Show the calculated shipping cost
print(f"Your estimated total for shipping this package is: ${delivery_cost:.2f}")
print("Thank you!") 