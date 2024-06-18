# Body Shape Classifier for Males ('m')

def determine_male_body_shape(height, chest, waist, hips):
    height_range = height / 6  # Adjust this factor based on your preference
    if abs(chest - hips) < height_range and abs(waist - chest) > height_range and abs(waist - hips) > height_range:
        return "Rectangle"
    elif chest < hips and waist < hips:
        return "Triangle"
    elif chest > hips and waist < chest:
        return "Inverted Triangle"
    elif abs(chest - hips) < height_range and waist < chest and waist < hips:
        return "Hourglass"
    else:
        return "Oval"

# Display header
print("Welcome to the Male Body Shape Classifier")
print("This program determines your body shape based on your height, chest, waist, and hip measurements.\n")

# Get measurements for male
height = float(input("Enter height (in inches): "))
chest = float(input("Enter chest measurement (in inches): "))
waist = float(input("Enter waist measurement (in inches): "))
hips = float(input("Enter hip measurement (in inches): "))

# Determine male body shape
body_shape = determine_male_body_shape(height, chest, waist, hips)

# Output the result
print(f"\nBased on your measurements, your body shape is: {body_shape}")
