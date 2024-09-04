# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. 
# The function should take the original price (price) and the discount percentage (discount_percent) as parameters. 
# If the discount is 20% or higher, apply the discount; otherwise, return the original price.



# The formula
def calculate_discount(price, discount_percent):
    # Checking to see if the discount percentage is more than 20%.
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Subtract the discount amount from the original price to get the final price
        final_price = price - discount_amount
    else:
        # If the discount is less than 20%, return the original price
        final_price = price
    
    return final_price

# Prompt the user to enter the original price of the item
price = float(input("2000"))

# Prompt the user to enter the discount percentage
discount_percent = float(input("15%"))

# Calculate the final price using the calculate_discount function
final_price = calculate_discount(price, discount_percent)

# Print the final price after applying the discount, or the original price if no discount was applied
if discount_percent >= 20:
    print(f"The final price after applying the discount is: ${final_price:.2f}")