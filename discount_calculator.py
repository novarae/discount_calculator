def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price, True   # return both the price and a flag (True = discount applied)
    return price, False  # no discount applied


# Prompt the user for input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Call the function
final_price, discount_applied = calculate_discount(original_price, discount_percentage)

# Print results 
if discount_applied:
    print(f"A discount of {discount_percentage}% was applied.")
    print(f"The final price after discount is: {final_price}")
else:
    print("No discount applied.")
    print(f"The price remains: {final_price}")
