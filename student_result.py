def calculate_result():
    while True:
        name = input("\nEnter student's name (or type 'Exit' to quit): ")
        
        if name.strip().lower() == "exit":
            print("Exiting program...")
            break
            
        try:
            mark1 = float(input("Enter mark for Subject 1: "))
            mark2 = float(input("Enter mark for Subject 2: "))
            mark3 = float(input("Enter mark for Subject 3: "))
            
            average = (mark1 + mark2 + mark3) / 3
            
            grade = ""
            if average >= 75:
                grade = "A"
            elif average >= 60:
                grade = "B"
            elif average >= 40:
                grade = "C"
            else:
                grade = "Fail"

            print("\n" + "-" * 30)
            print(f"Name   : {name}")
            print(f"Average: {average:.1f}")
            print(f"Grade  : {grade}")
            print("-" * 30)
                
        except ValueError:
            print("Error: Please enter valid numerical marks.")

if __name__ == "__main__":
    calculate_result()
