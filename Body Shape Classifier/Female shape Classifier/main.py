# Body Shape Classifier for Females ('f')

def determine_female_body_shape(height, bust, waist, hips):
    height_range = height / 6  # Adjust this factor based on your preference
    if abs(bust - hips) < height_range and abs(waist - bust) > height_range and abs(waist - hips) > height_range:
        return "Rectangle"
    elif bust < hips and waist < hips:
        return "Pear"
    elif bust > hips and waist < bust:
        return "Apple"
    elif abs(bust - hips) < height_range and waist < bust and waist < hips:
        return "Hourglass"
    else:
        return "Round"

# Display header
print("Welcome to the Female Body Shape Classifier")
print("This program determines your body shape based on your height, bust, waist, and hip measurements.\n")

# Get measurements for female
height = float(input("Enter height (in inches): "))
bust = float(input("Enter bust measurement (in inches): "))
waist = float(input("Enter waist measurement (in inches): "))
hips = float(input("Enter hip measurement (in inches): "))

# Determine female body shape
body_shape = determine_female_body_shape(height, bust, waist, hips)

# Output the result
print(f"\nBased on your measurements, your body shape is: {body_shape}")
