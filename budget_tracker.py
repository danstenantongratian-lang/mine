def main():
    try:
        # Ask for total monthly budget
        total_budget = float(input("Enter your total monthly budget: "))

        expenses = []
        # Ask for expenses until "done" is typed
        while True:
            user_input = input("Enter an expense (or type 'done' to finish): ").lower()
            if user_input == 'done':
                break
            try:
                expense = float(user_input)
                expenses.append(expense)
            except ValueError:
                print("Invalid input. Please enter a number or 'done'.")

        # Calculate remaining balance
        total_expenses = sum(expenses)
        remaining_balance = total_budget - total_expenses

        # Display results
        print(f"\nTotal Budget: ${total_budget:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Remaining Balance: ${remaining_balance:.2f}")

        # Check for low funds
        if remaining_balance < 500:
            print("Warning: Low Funds")

    except ValueError:
        print("Error: Please enter valid numeric values.")

if __name__ == "__main__":
    main()
