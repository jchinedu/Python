total_miles = 0.0
total_gallons = 0.0

while True:
    gallons = float(input("Enter the gallons used (-1 to end): "))
    
    if gallons == -1:
        break
    
    miles = float(input("Enter the miles driven: "))
    
    mpg = miles / gallons
    print(f"The miles/gallon for this tank was {mpg:.6f}")
    
    total_gallons += gallons
    total_miles += miles

if total_gallons > 0:
    overall_mpg = total_miles / total_gallons
    print(f"The overall average miles/gallon was {overall_mpg:.5f}")
else:
    print("No valid data entered.")
 