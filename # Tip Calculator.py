# Tip Calculator
user_input = input("Enter the total bill amount: $")
bill_amount = float(user_input)
tip_percentage = 0.18
sale_tax_percentage = 0.07
tip_amount = bill_amount * tip_percentage
sale_tax_amount = bill_amount * sale_tax_percentage
total_amount = bill_amount + tip_amount + sale_tax_amount  
print(f"Tip Amount: ${tip_amount:.2f}")
print(f"Sales Tax Amount: ${sale_tax_amount:.2f}")
print(f"Total Amount: ${total_amount:.2f}")