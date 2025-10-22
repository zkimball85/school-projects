print("Welcome to the Café, Thank you for coming!")
    
drink_price = float(input("Enter the price of your drink: $"))
food_price = float(input("Enter the price of your food: $"))
tip_amount = float(input("Enter your tip amount: $"))

membership_card = input("Did you use a membership card? (yes/no): ").lower().strip()

subtotal = drink_price + food_price + tip_amount

is_member = membership_card == "yes"

discount_percentage = 0.0
loyalty_points_multiplier = 0.0
description = "Standard Purchase"

if is_member and subtotal > 25:
    discount_percentage = 0.15
    loyalty_points_multiplier = 1.5
    description = "Premium customer tier"

elif is_member and 10 <= subtotal <= 25:
    discount_percentage = 0.10
    loyalty_points_multiplier = 1.0
    description = "Standard member reward"

elif not is_member and subtotal > 25:
    discount_percentage = 0.05
    loyalty_points_multiplier = 0.5
    description = "One-time thank-you offer"

elif not is_member and subtotal < 10:
    discount_percentage = 0.0
    loyalty_points_multiplier = 0.25
    description = "First-time customer bonus"

else:
    discount_percentage = 0.0
    loyalty_points_multiplier = 0.5 
    description = "Standard purchase"

discount_amount = subtotal * discount_percentage
total = subtotal - discount_amount
loyalty_points = subtotal * loyalty_points_multiplier

print("\n--- Café Checkout Summary ---")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount: ${discount_amount:.2f}")
print(f"Total After Discount: ${total:.2f}")
print(f"Member: {'Yes' if is_member else 'No'}")
print(f"Loyalty Points Earned: {loyalty_points:.1f}")
print(f"Reward Tier: {description}")
print("-------------------------------")

