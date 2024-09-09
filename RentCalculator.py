import datetime
import matplotlib.pyplot as plt

def calculate_expenses(num_occupants):
    # Base rent for the entire room
    base_rent = float(input("Enter the base rent for the room per month: "))

    # Shared expenses
    shared_expenses = []
    while True:
        expense_name = input("Enter a shared expense name (or 'done' to finish): ")
        if expense_name.lower() == "done":
            break
        expense_amount = float(input(f"Enter the amount for {expense_name} per month: "))
        shared_expenses.append((expense_name, expense_amount))

    # Recurring expenses
    recurring_expenses = []
    while True:
        expense_name = input("Enter a recurring expense name (or 'done' to finish): ")
        if expense_name.lower() == "done":
            break
        expense_amount = float(input(f"Enter the monthly amount for {expense_name} per month: "))
        recurring_expenses.append((expense_name, expense_amount))

    # Get total charges for food, water, and electricity
    total_food_charges = float(input("Enter the total food charges per month: "))
    total_water_charges = float(input("Enter the total water charges per month: "))
    total_electricity_charges = float(input("Enter the total electricity charges per month: "))

    # Calculate per-person charges
    per_person_food_charges = round(total_food_charges / num_occupants)
    per_person_water_charges = round(total_water_charges / num_occupants)
    per_person_electricity_charges = round(total_electricity_charges / num_occupants)

    # Calculate total expenses
    total_expenses = total_food_charges + total_water_charges + total_electricity_charges
    per_person_total_expenses = round(total_expenses / num_occupants)

    # Savings goals
    savings_goal = float(input("Enter your monthly savings goal: "))
    monthly_income = float(input("Enter your monthly income: "))
    savings_progress = monthly_income - total_expenses

    # Graphical representation
    labels = ["Rent", "Food", "Water", "Electricity", "Shared Expenses", "Recurring Expenses"]
    values = [base_rent, total_food_charges, total_water_charges, total_electricity_charges, sum(amount for _, amount in shared_expenses), sum(amount for _, amount in recurring_expenses)]

    # Ensure all values are numerical before plotting
    values = [float(val) for val in values]  # Convert to floats if necessary

    plt.pie(values, labels=labels, autopct="%1.1f%%")
    plt.title("Expense Breakdown")
    plt.show()

    plt.bar(labels, values)
    plt.xlabel("Expense Category")
    plt.ylabel("Amount")
    plt.title("Expense Breakdown (Bar Chart)")
    plt.show()

    print("Total Rent:", base_rent)
    print("Monthly Food Charges Per Person:", per_person_food_charges)
    print("Monthly Water Charges Per Person:", per_person_water_charges)
    print("Monthly Electricity Charges Per Person:", per_person_electricity_charges)
    print("Total Monthly Expenses Per Person:", per_person_total_expenses)
    print("Savings Progress Per Month:", savings_progress)

    # Brief summary
    print("\nExpense Summary:")
    print(f"Total Monthly Expenses: {round(total_expenses)}")
    print(f"Per Person Total Monthly Expenses: {per_person_total_expenses}")
    print(f"Savings Progress Per Month: {round(savings_progress)}")

# Get the number of occupants from the user
num_occupants = int(input("Enter the number of occupants: "))

# Calculate expenses
calculate_expenses(num_occupants)