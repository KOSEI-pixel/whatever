def calculate_due_amount(total_bill, amount_paid):
    if amount_paid >= total_bill:
        return 0
    else:
        return total_bill - amount_paid
    
def main():
    total_bill = float(input("Enter the total bill amount: "))
    amount_paid = float(input("Enter the amount paid: "))

    due_amount = calculate_due_amount(total_bill, amount_paid)
    print(f"The due amount is: {due_amount}")

if __name__ == "__main__":
    main()

