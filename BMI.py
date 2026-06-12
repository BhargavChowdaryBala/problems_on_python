w=int(input("Enter your weight in kg "))
h=float(input("Enter your height in m "))

bmi=w/(h**2)
if (bmi<18.5):
    print("Underweight")
elif (bmi>=18.5 and bmi<24.9):
    print("Normal")
elif(bmi>=25 and bmi<28.9):
    print("Overweight")
else:
    print("Obesity")
