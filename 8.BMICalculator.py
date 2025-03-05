# Python program for BMI Calculator(Body Mass Index)
def convert_height(height,unit):
    if unit =="feet":
        return height*0.3048 #convert feet to meters
    return height
def convert_weight(weight,unit):
    if unit.lower() =="lbs":
        return weight * 0.453592 #convert lbs(pound) to kg
    return weight
def bmi_calcuate(height,weight):
    return weight /(height ** 2)
def get_bmi_category(bmi):
    if bmi<18.5:
        return "UnderWeight"
    elif 18.5<= bmi<=24.9:
        return "Normal Weight"
    elif 25<=bmi<=29.9:
        return "OverWeight"
    elif 30<= bmi <=39.9:
        return "Obese"
    else:
        return "Severely Obese"
def main():
    while True:
        height=eval(input("Enter your Height:"))
        height_unit = input("Is your height in meters or feet? ")
        weight=eval(input("Enter your Weight:"))
        weight_unit = input("Is your weight in kg or lbs? ")

        #convert units
        height_m=convert_height(height,height_unit)
        weight_kg=convert_weight(weight,weight_unit)

        # Calculate BMI
        bmi =bmi_calcuate(height_m,weight_kg)
        category=get_bmi_category(bmi)

        print(f"Your BMI is {bmi:.2f},which falls under the category:{category}.")

        choice = input("Do you want to calculate again? (yes/no): ").strip().lower()
        if choice != "yes":
            print("Exiting the program. Goodbye!")
            break
if __name__=="__main__":
    main()


