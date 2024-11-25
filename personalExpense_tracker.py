import json

def load_expenses(filename="expenses.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return{}
    except json.JSONDecodeError:
        print("Error: file is corrupted. Starting with an empty expense list.")
        return{}
    
def save_expenses(expenses, filename="expenses.json"):
        with open(filename, "w") as file:
            json.dump(expenses, file, indent=4)

def add_expense(expenses):
        category = input("Enter the category (e.g., Food, Rent, Entertainment):")
        try:
            amount = float(input("Enter the amount: "))
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            return
        
        if category in expenses:
            expenses[category].append(amount)
        else:
            expenses[category] = [amount]

        print(f"Added {amount} to {category}.")

def view_expenses(expenses):
     if not expenses:
          print("No expenses recorded yet.")
          return 
     
     print("\nExpenses Summary:")
     total = 0
     for category, amounts in expenses.items():
         category_total = sum(amounts)
         print(f" - {category}: {category_total:.2f}")
         total += category_total
         print(f"Total Expenses: {total:.2f}")

def delete_expenses(expenses):
    try:
        category = input("Enter the category to delete or modify: ")  # Prompt for the category
        if category not in expenses:
            print("Category not found.")
            return
        print(f"Expenses in {category}: {expenses[category]}")
        
        print("1. Delete the entire category")
        print("2. Delete a specific expense")
        choice = int(input("Enter your choice:"))

        if choice == 1:
            del expenses[category]
            print(f"Deleted category {category}.")
        elif choice == 2:
            expense_index = int(input("Enter the index of the expense to delete (starting from 0): "))
            if 0 <= expense_index < len(expenses[category]):
                deleted = expenses[category].pop(expense_index)
                print(f"Deleted expense {deleted} from {category}")

                if not expenses[category]:
                    del expenses[category]
            else:
                print("Invalid index.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input.")


# Main program

if __name__ == "__main__":
     print("Welcome to the Personal Expense tracker! ")

     expenses = load_expenses()

     while True:
          print("\nOptions:")
          print("1. Add expense")
          print("2. View Expenses")
          print("3. Delete Expense")
          print("4. Exit")

          try:
               choice=int(input("Enter your choice: "))
          except ValueError:
               print("Invalid input. Please enter a number between 1 and 4.")
               continue
          if choice == 1:
               add_expense(expenses)
               save_expenses(expenses)
          elif choice == 2:
               view_expenses(expenses)
          elif choice == 3:
               delete_expenses(expenses)
               save_expenses(expenses)
          elif choice == 4:
               save_expenses(expenses)
               print("Goodbye")
               break
          else:
               print("Invalid choice. please try again. ")



             
    