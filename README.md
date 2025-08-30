
A simple Python discount calculator that applies discounts of 20% or more, built to practice functions and conditionals.
# 🛒 Discount Calculator (Python)

## 📌 Overview
This project is a simple Python program that calculates the final price of an item after applying a discount.  

It includes a function named **`calculate_discount(price, discount_percent)`** which:  
- Applies the discount if the percentage is **20% or higher**  
- Returns the original price if the discount is **less than 20%**  

The program also prompts the user for input and displays the final price.

---

## ⚙️ How It Works
1. The user enters the original price of an item.  
2. The user enters the discount percentage.  
3. The program checks if the discount is ≥ 20%.  
   - If yes → applies the discount.  
   - If no → returns the original price.  
4. The final result is printed to the screen.  

---

## 💻 Example Usage

**Case 1: Discount Applied (≥ 20%)**
```bash
Enter the original price of the item: 200
Enter the discount percentage: 25
A discount of 25.0% was applied.
The final price after discount is: 150.0
