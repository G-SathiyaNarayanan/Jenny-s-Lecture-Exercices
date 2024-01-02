height= float(input("Enter the Height: "))
weight= float(input("Enter the Weight: "))
bmi= round(weight/(height ** 2))
print("The BMI is: ", bmi)
if bmi<18:
  print(f"Your BMI is  {bmi} and you are conidered as Underweight")
elif bmi<25:
    print(f"Your BMI is  {bmi} and you are conidered as Normal Weight")
elif bmi<30:
  print(f"Your BMI is  {bmi} and you are conidered as Over Weight")
elif bmi<35:
    print(f"Your BMI is  {bmi} and you are conidered as Obese Weight")
else:
  print(f"Your BMI is  {bmi} and you are conidered as Clinically Obese Weight")
