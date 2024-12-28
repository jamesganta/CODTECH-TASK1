def calculate_bmi(weight, height):
  """
  Calculates the Body Mass Index (BMI).

  Args:
    weight: Weight in kilograms.
    height: Height in meters.

  Returns:
    The calculated BMI.
  """
  return weight / (height * height)

def get_bmi_category(bmi):
  """
  Determines the BMI category based on the calculated BMI.

  Args:
    bmi: The calculated BMI value.

  Returns:
    The BMI category as a string.
  """
  if bmi < 18.5:
    return "Underweight"
  elif bmi < 25:
    return "Normal"
  elif bmi < 30:
    return "Overweight"
  else:
    return "Obese"

# Get user input
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = calculate_bmi(weight, height)

# Determine BMI category
category = get_bmi_category(bmi)

# Display results
print(f"Your BMI is: {bmi:.2f}")
print(f"BMI Category: {category}")