Overview
This Python program helps manage and calculate shared living expenses for a group of occupants (e.g., roommates). It allows users to:

Calculate shared rent, utilities, and recurring expenses.
Split these expenses among a specified number of occupants.
Track personal savings goals based on income and expenses.
Generate visual representations (pie chart and bar chart) of the expense breakdown.
Features
Base Rent Calculation: Prompts the user to enter the base rent for the room, which is equally divided among all occupants.

Shared Expenses: Allows users to input shared expenses (e.g., cleaning services, common household items) which are split among all occupants.

Recurring Expenses: Users can add other recurring expenses (e.g., subscriptions, maintenance fees) to be included in the expense breakdown.

Utility Charges: Prompts for total monthly charges for food, water, and electricity, which are then divided equally among the occupants.

Savings Goal: Users can set a monthly savings goal and provide their monthly income to track their savings progress based on the calculated expenses.

Graphical Visualization:

A Pie Chart that shows the percentage breakdown of rent, utilities, shared expenses, and recurring expenses.
A Bar Chart that shows the total amount for each expense category.
Summary Report: Provides a brief summary of:

Total monthly expenses per person.
The user’s savings progress based on their savings goal and income.
How to Run the Program
Ensure you have Python 3 installed along with the matplotlib library. You can install matplotlib by running:

bash
pip install matplotlib
Copy the provided code into a Python file (e.g., shared_expense_tracker.py).

Run the script by executing:

bash
python shared_expense_tracker.py
Follow the on-screen prompts to input expenses, income, and savings goals.

Input Details
Base Rent: The total rent for the living space.
Shared Expenses: These are costs shared equally among all occupants, such as cleaning services or common household items. The program allows users to enter multiple shared expenses.
Recurring Expenses: These are regular expenses that occur every month (e.g., internet subscription, gym membership).
Utility Charges: Total food, water, and electricity charges for the household, which are divided among all occupants.
Number of Occupants: This is the total number of people sharing the living space, which will determine how the costs are split.
Savings Goal and Income: The user’s savings goal and monthly income to track how much they can save after all expenses are deducted.
Output
Expense Breakdown: Displays the total rent, food, water, and electricity charges per person, along with the total expenses for each category.
Savings Progress: Shows the amount left after all expenses, which can be allocated to savings.
Pie Chart: Visual representation of the distribution of expenses.
Bar Chart: Graphical view showing the amount spent in each expense category.
Example Usage
bash
Enter the number of occupants: 4
Enter the base rent for the room per month: 1200
Enter a shared expense name (or 'done' to finish): Cleaning
Enter the amount for Cleaning per month: 100
Enter a shared expense name (or 'done' to finish): done
Enter a recurring expense name (or 'done' to finish): Internet
Enter the monthly amount for Internet per month: 60
Enter a recurring expense name (or 'done' to finish): done
Enter the total food charges per month: 400
Enter the total water charges per month: 50
Enter the total electricity charges per month: 150
Enter your monthly savings goal: 300
Enter your monthly income: 2500

[ Pie chart and bar chart of expenses appear ]

Total Rent: 1200.0
Monthly Food Charges Per Person: 100
Monthly Water Charges Per Person: 12
Monthly Electricity Charges Per Person: 37
Total Monthly Expenses Per Person: 200
Savings Progress Per Month: 2300

Expense Summary:
Total Monthly Expenses: 600
Per Person Total Monthly Expenses: 200
Savings Progress Per Month: 2300
Dependencies
Python 3.x
Matplotlib: Required for generating graphical representations of expenses. Install it using:
bash
pip install matplotlib
Future Improvements
Add functionality for editing or deleting individual expenses.
Include an option to handle one-time expenses in addition to monthly recurring expenses.
Provide an option to export the expense summary and graphs to a PDF or CSV file for sharing.
